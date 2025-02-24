import random
import string

class CreateKey:

    def __init__(self):
        chars = string.punctuation + string.digits + string.ascii_letters + " "  # המשתנה הזה הוא סטרינג אחד ארוך. אותיות,מספרים וכו'
        chars = list(chars)  # ממיר את הסטרינג לרשימה. כל תו, איבר ברשימה.
        self.key = chars.copy()  # עותק של הרשימה
        random.shuffle(self.key)  # פונקציה ברנדום שלוקחת את הרשימה ומערבבת את הסדר שלהם
        with open("current key", "w") as f:
            f.write(str(self.key))