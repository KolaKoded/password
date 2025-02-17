# Building a Password Manager 

import os
path = 'passwords.txt'

print("WELCOME TO PASSWORD MANAGER!")
print("This service lets you save your username and password.")

def save_pw ():
    file_check = os.path.exists(path)
    try: 
        with open(path, 'r') as file:
            print("The file exists.")
    except FileNotFoundError:
        print("The password file does not exist. Creating file...")
        file = open("passwords.txt", "w");

    account_name = input("Enter the name of account: ")
    password = input("Enter your password: ")
    details = ['account:' + account_name, 'password:' + password]
    print (details)
    try:
        with open(path, 'w') as file:
            for account in details:
                file.write("%s\n" % account)
        print("Your password for " + account_name + " is saved succesfully!")
    except Exception as e:
        print("Oops! Can't save password. Error: {e}")
    

save_pw()