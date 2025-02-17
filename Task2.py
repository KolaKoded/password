#Designing my UBA USSD APPLICATION

# Initial balance and bank USSD PIN
PIN = "0000"      # PIN - Global variable
Balance = 1000    # Balance - Global variable

def buy_airtime(PIN, Balance):
    try:
        option = input("1. Airtime Self\n2. Airtime Others: ")  # option - Local variable
        if option == "1" or "2":
            phone_number = input("Enter the phone number: ")  # phone_number - Local variable
            amount = int(input("Enter the amount: ₦"))       #    amount - Local variable
            user_PIN = input("Enter your Bank PIN: ")          #   PIN - Local variable
            if user_PIN == PIN:
                    Balance -= amount                        # Balance  - Local variable
                    print("Airtime purchase of ₦" + str(amount) + " for " + phone_number + " was successful. Your new account balance is #" + str(Balance) + ". Thank you!")
                    exit_uba(PIN, Balance)
            else: 
                    print("Wrong PIN. Try again!")
                    exit_uba(PIN, Balance)
        else:
            print("option is invalid")
    except ValueError:
         print("Input is invalid. Kindly enter a valid number for the options")
         exit_uba(PIN, Balance)


def buy_data(PIN, Balance):
    print("You selected Buy Data.")
    phone_number = input("Enter the phone number: ")           # phone_number - Local variable
    amount = input("Enter the data amount (e.g., 1GB, 5GB): ")   # amount - Local variable
    PIN = input("Enter your Bank PIN: ")                        #   PIN - Local variable
    if PIN == PIN:
        print("Data purchase of " + amount + "GB for " + phone_number + " was successful.")
        exit_uba(PIN, Balance)
    else: 
        print("Wrong PIN. Try again!")
        exit_uba(PIN, Balance)   

def transfers(PIN, Balance):
    try:
        account_number = int(input("Enter the account number: "))  # account_number  - Local variable
    except ValueError:
        print("Kindly enter a valid account number")
        exit_uba(PIN, Balance)
    try:
        amount = int(input("Enter the transfer amount: ₦"))   # amount - Local variable
    except ValueError:
        print("Kindly enter a valid transfer amount!")
        exit_uba(PIN, Balance)

    user_PIN = input("Enter your Bank PIN: ")         #   PIN - Local variable
    if user_PIN == PIN:
            Balance -= amount                           # Balance  - Local variable
            print("Transfer of ₦" + str(amount) + " to account number " + str(account_number) + " was successful. Your new account balance is #" + str(Balance) + ". Thank you!")
            exit_uba(PIN, Balance)
    else:
            print("Wrong PIN. Try again!")
    #except ValueError:
        #print("Input is invalid. Kindly enter a valid number for the options")
    exit_uba(PIN, Balance)
    
def pay_bills(PIN, Balance):
    bill_type = input("Enter the bill type (e.g., electricity, water): ")  # bill_type  - Local variable
    amount = int(input("Enter the amount: ₦"))                  #  amount  - Local variable
    PIN = input("Enter your Bank PIN: ")                        # PIN  - Local variable
    if PIN == PIN:
        Balance -= amount                                       # Balance  - Local variable
        print("Payment of ₦" + str(amount) + " for " + bill_type + " was successful.")
        exit_uba(PIN, Balance)
    else:
        print("Wrong PIN. Try again!")
        exit_uba(PIN, Balance)


def check_balance(PIN, Balance):  
    PIN = input("Enter your Bank PIN: ")                               # PIN  - Local variable
    if PIN == PIN:
        print("Your current balance is: ₦" + str(Balance) + ".")
        exit_uba(PIN, Balance)
    else:
        print("Wrong PIN. Try again!")
        exit_uba(PIN, Balance)

def get_credit(PIN, Balance):
    amount = int(input("Enter the credit amount you want to borrow: ₦"))       # amount      - Local variable
    PIN = input("Enter your Bank PIN: ")                             # PIN  - Local variable
    if PIN == PIN:
        Balance += amount                                                 # Balance  - Local variable
        print("Your request to borrow ₦" + str(amount) + " is succesful. Your current balance is: ₦" + str(Balance) + ".")
        exit_uba(PIN, Balance)
    else:
        print("Wrong PIN. Try again!")
        exit_uba(PIN, Balance)    

def enquiries(PIN, Balance):
    print("For assistance, contact customer care at 0800-123-4567.")
    exit_uba(PIN, Balance)

def exit_uba(PIN, Balance):
    option = input ("Do you want to continue(yes/no): ")      # option     - Local variable
    if option == "yes":
    
        ussd_menu(PIN, Balance)
    else:
        print("Thank you for using the UBA Banking Service. Goodbye!")
        return # RETURN statement added

def ussd_menu(PIN, Balance):
    try:
        print("Welcome to the USSD Banking Service")
        print("Please select an option:")
        print("1. Buy Airtime\n2. Buy Data\n3. Transfers\n4. Pay Bills\n5. Check Balance\n6. Get Credit\n7. Enquiries\n8. Exit")
        option = input("Enter your option: ")                        # option     - Local variable
        if option == "1":
                buy_airtime(PIN, Balance)
                return # RETURN statment added
        elif option == "2":
                buy_data(PIN, Balance)
                return # RETURN statment added
        elif option == "3":
                transfers(PIN, Balance)
                return # RETURN statment added
        elif option == "4":
                pay_bills(PIN, Balance)
                return # RETURN statment added
        elif option == "5":
                check_balance(PIN, Balance)
                return # RETURN statment added
        elif option == "6":
                get_credit(PIN, Balance)
                return # RETURN statment added
        elif option == "7":
                enquiries(PIN, Balance)
                return # RETURN statment added
        elif option == "8":
                exit_uba(PIN, Balance)
                return # RETURN statment added
        else:
                print("Invalid option. Please try again.")
    except ValueError:
            print("Invalid input. Please enter a number out of the options.")
            ussd_menu(PIN, Balance)
         

# Main Bank Function
def UBA_bank(PIN, Balance): 
    ussd_code = input("Enter your USSD code: ")        # ussd_code - Local variable
    
    if ussd_code == "*919#":
        ussd_menu(PIN, Balance)
    else:
        print("Invalid USSD code. Please dial *919# to access this service.")
        return # RETURN statment instead of UBA_bank(PIN, Balance)

# Run the application
UBA_bank(PIN, Balance)