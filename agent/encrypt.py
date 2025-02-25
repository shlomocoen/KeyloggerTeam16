import string
class Encryption:

    def __init__(self,text,key):           #  המחלקה מקבלת טקסט להצפנה ומפתח המורכב מרשימה מעורבבת של chars
        self.original_text = text
        self.key = key

    def encrypt_text(self):
        changed_text = ""     # מאתחל משתנה שיחזיק את הטקסט המוצפן
        chars = string.punctuation + string.digits + string.ascii_letters + " "     #המשתנה הזה הוא סטרינג אחד ארוך. אותיות,מספרים וכו'
        chars = list(chars)       #  ממיר את הסטרינג לרשימה. כל תו, איבר ברשימה.

        for letter in self.original_text:
            try:#  עובר על הטקסט
                index = chars.index(letter)     #  מגדיר משתנה אינדקס ששומר את המיקום של התו הנוכחי
                changed_text += self.key[index]  #   מוצא את המקביל שלו ברשימה השנייה ומוסיף אותו לטקסט המוצפן
            except:
                changed_text += letter

        return changed_text




