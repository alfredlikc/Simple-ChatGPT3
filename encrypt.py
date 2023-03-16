# This script encrypts logins and passwords onto a login.pass file

import base64

passwords = open("login.pass", "w", encoding = "ASCII") # open txt

encoding = {"alfredlikc": "Cans1974", "rian": "12100F", "christoph": "gtx1650", "ay": "laptopsbad", "M": "pentiumFTW"}

for i in encoding.keys():
    passwords.write(base64.b64encode(i.encode('utf-8')).decode('utf-8') + "\n")
    passwords.write(base64.b64encode(encoding[i].encode('utf-8')).decode('utf-8') + "\n")

passwords.close()