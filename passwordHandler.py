# This script allows you to get a user login and validate with encrypted info

import base64, getpass


passwords = open("login.pass", "r", encoding = "ASCII") # opens password encrypted file
logins = {} # creates a dictionary for logins

lines = passwords.read().splitlines() # puts each line into list
for i in range(0, len(lines), 2): # for every user
    logins[lines[i]] = lines[i+1] # add to dictionary

passwords.close() # closes password encrypted file


# Asks user for login and checks against encrypted info
def loginCheck():
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    encodedUsername = base64.b64encode(username.encode("UTF-8")).decode("UTF-8")
    encodedPassword = base64.b64encode(password.encode("UTF-8")).decode("UTF-8")


    if encodedUsername in logins.keys():
        if encodedPassword == logins[encodedUsername]:
            return True, username
    
    return False, username