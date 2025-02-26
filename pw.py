# Building a Password Manager 

import os    #Importing os module
path = 'passwords.txt' #define path for file where passwords will be saved

print("WELCOME TO PASSWORD MANAGER!")   #User welcome message
print("This service lets you save your username and password.")

#Define a function to save passw
def save_pw ():
    #file_check = os.path.exists(path) #checking if file exists
    try: 
        with open(path, 'r') as file:   #open the file in read mode 
            print("The file exists.")
    except FileNotFoundError:
        print("The password file does not exist. Creating file...") #Create a new file "passwords.txt" in write mode ("w") if not exist
        file = open("passwords.txt", "w");
    #taking user input for credentials
    account_name = input("Enter the name of account: ")
    password = input("Enter your password: ")
    details = ['account:' + account_name, 'password:' + password] #storing user input in a list
    print (details) #print user credentials to confirm befroe saving 
    try:
        with open(path, 'a') as file: #open file in append mode to add new passwords
            for account in details: #loops through the list and writes each item as a new line
                file.write("%s\n" % account)
        print("Your password for " + account_name + " is saved succesfully!") #Prints a success message after saving
    except Exception as e:
        print(f"Oops! Can't save password. Error: {e}") #handling any unexpected errors while appending to file 

save_pw()