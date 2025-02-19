import base64


class XorEncryptor:

    def __init__(self, encryption_key: str):
        self.encryption_key = encryption_key#.encode()

    def encryption_information(self, text: str):
        encrypted_information = []
        #text = text.encode()
        index = 0
        while index < len(text):
            for w in self.encryption_key:
                if index < len(text):
                    #encrypted_information += bytes(ord(text[index]) ^ ord(w))
                    encrypted_information.append(ord(text[index]) ^ ord(w))
                    index += 1

        #return encrypted_information
        encrypted_information = bytearray(encrypted_information)
        return base64.urlsafe_b64encode(encrypted_information).decode('utf-8')


    def decoding_information(self, text: str):
        text = base64.urlsafe_b64decode(text.encode('utf-8'))
        print(text)
        decoded_information = ""
        index = 0
        while index < len(text):
            for w in self.encryption_key:
                if index < len(text):
                    decoded_information += chr(text[index] ^ ord(w))
                    #print(text[index],"==", decoded_information[index])
                    index += 1
                    # print(len(decoded_information),"D:" ,decoded_information)
        #decoded_information = bytes(decoded_information)
        return decoded_information




    # def xor_encrypt(self, text, key):
    #     xored = ''.join(
    #         chr(ord(x) ^ ord(y)) for x, y in zip(text, key * (len(text) // len(key)) + key[:len(text) % len(key)])
    #     )
    #     return xored


x = XorEncryptor("abcd")
with open("keylogger_new.txt", "r") as f:
      a = f.read()
print(a)
print(x.decoding_information(a))
# y = x.encryption_information("Hello, world!")
# print(y, "1")
# # print(type(y))
# print(x.decoding_information(y), 2)
# f = open("keylogger.txt")
# a = ""
# for i in f:
#     a += i
# f.close()
# with open("keylogger.txt") as f:
#     a = f.read()
# print(a)
# print("-----------------------------------------")
# print(x.decoding_information(a))
# print("----------------------------------------")
# print(x.decoding_information("ABCnPQLVNPSVTBRP[PW^AhBCD 	B(L;BCEABBDACCD@BCEABBDACCD@BCDA A)O"))
# print("-----------------------------------------")
# print(x.decoding_information("PQLVNPSVTBRP[PP^Ah\nDABDABABC\nDAB\nABC CDA\niPQLVNPSVTBRP[PP^Ah	ABCCDA\n BCDAPCDPBCDACDABCBCD\n\n\nBCD\nCDA DAB\n\nABCnPQLVNPSVTBRP[PW^AhBCD 	B(L;BCEABBDACCD@BCEABBDACCD@BCDA A)O\n<AB#Dk"))

#
# b = x.decoding_information("PQLVNPSVTBRP[WV^Ah D\nBA	B\nA\niPQLVNPSVTBRP[WV^Ah	A")
# print(b)

import base64

def xor_cipher(text: str, key: str) -> str:
    encrypted_bytes = [ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(text)]
    #print(encrypted_bytes)
    encrypted_bytes = bytearray(encrypted_bytes)
    return base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')

def xor_decipher(encoded_text: str, key: str) -> str:
    encrypted_bytes = base64.urlsafe_b64decode(encoded_text.encode('utf-8'))
    return ''.join(chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(encrypted_bytes))

# key = "mysecret"
# text = "Hello, World!"
#
# encrypted = xor_cipher(text, key)
# print("Encrypted:", encrypted)
#
#
# decrypted = xor_decipher(encrypted, key)
# print("Decrypted:", decrypted)
#
# # בדיקה האם הפענוח מחזיר את הטקסט המקורי
# assert decrypted == text, "Decryption failed!"
#
# with open("keylogger_new.txt", "r") as f:
#     a = f.read()
# print(xor_decipher(a, "abcd"))

