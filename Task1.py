#ATM Machine 

# Initial balance
balance = 100 # balance - Global variable

def check_balance(balance):
    print("Your current balance is: ₦" + str(balance) + "!")
    exit_atm(balance)

def deposit(balance):
    amount = int(input("Enter the amount to deposit: ₦"))
    if amount > 0:
            balance += amount
            print("₦" + str(amount) + " deposited successfully. Your new balance is ₦" + str(balance) + "!")
            exit_atm(balance)
    else:
        print("Invalid amount. Please enter a valid deposit.")
    return balance

def withdraw(balance):
    amount = int(input("Enter the amount to withdraw: ₦"))
    if 0 <= amount <= balance:
            balance -= amount
            print("₦" + str(amount) + " withdrawn successfully. Your new balance is ₦" + str(balance) + "!")
            exit_atm(balance)
    elif amount > balance:
            print("Insufficient funds.")
            exit_atm(balance)
    else:
        print("Invalid amount. Please enter a withdrawal amount.")
        exit_atm(balance)

    return balance

def atm_machine(balance):
    print("Welcome to your bank account!")
    print("\nSelect an option: \n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4.Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        check_balance(balance)
    elif option == 2:
        deposit(balance)
    elif option == 3:
        withdraw(balance)
    elif option == 4:
        print("Thank you for using the ATM. Bye!")
    else:
        print("Invalid option. Please try again.")

def exit_atm (balance):
    option = input("Do you want to keep using the ATM yes/no: ")

    if option == "yes":
        atm_machine(balance)
    elif option == "no":
        print("Thank you for using the ATM!")

    else:
        print("Invalid option!")

# Run the ATM machine
atm_machine(balance)
