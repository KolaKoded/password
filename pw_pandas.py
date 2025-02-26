import pandas as pd #imports the Pandas library to handle user input, create DataFrames and save data into CSV

print("WELCOME TO PASSWORD MANAGER!") #User welcome message
print("This service lets you save your username and password.")

account_name = input("Enter the name of account: ") #Taking user input for the account name and a password
password = input("Enter your password: ")

details = {'account': [account_name],
           'password': [password]}  #User input is stored in a dictionary for account + password

print (details) #Prints the dictionary to confirm the user’s input before saving

df = pd.DataFrame(details) #Converting dictionary data into a pandas dataframe

#df.to_csv('passwords_data.csv', mode='a', header=True, index=False);
#print("Password saved successfully!"

try:
    df.to_csv('passwords_data.csv', mode='a', header=True, index=False)
    print("Password saved successfully!")
except Exception as e:
    print(f"Error while saving data: {e}")