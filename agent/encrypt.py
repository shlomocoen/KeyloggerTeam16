import random
import string
class Encryption:

    def __init__(self,text):           #  המחלקה מקבלת טקסט להצפנה
        self.original_text = text


    def encrypt_text(self):
        changed_text = ""     # מאתחל משתנה שיחזיק את הטקסט המוצפן
        chars = string.punctuation + string.digits + string.ascii_letters + " "     #המשתנה הזה הוא סטרינג אחד ארוך. אותיות,מספרים וכו'
        chars = list(chars)       #  ממיר את הסטרינג לרשימה. כל תו, איבר ברשימה.
        key = chars.copy()        #   עותק של הרשימה
        random.shuffle(key)       #   פונקציה ברנדום שלוקחת את הרשימה ומערבבת את הסדר שלהם

        for letter in self.original_text:    #  עובר על הטקסט
            index = chars.index(letter)      #  מגדיר משתנה אינדקס ששומר את המיקום של התו הנוכחי
            changed_text += key[index]       #   מוצא את המקביל שלו ברשימה השנייה ומוסיף אותו לטקסט המוצפן

        print(changed_text)



v = Encryption("i love pizza")
v.encrypt_text()





