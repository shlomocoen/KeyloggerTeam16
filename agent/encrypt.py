import random
import string
class Encryption:

    def __init__(self,text):
        self.original_text = text


    def encrypt_text(self):
        changed_text = ""
        chars = string.punctuation + string.digits + string.ascii_letters + " "
        chars = list(chars)
        key = chars.copy()
        random.shuffle(key)

        for letter in self.original_text:
            index = chars.index(letter)
            changed_text += key[index]

        print(changed_text)



v = Encryption("i love pizza")
v.encrypt_text()





