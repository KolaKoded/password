# create a variable called pin
# create a variable called userPin
# create a variable called userAge
# compare pin with userPin
# if the pin is correct, print "Welcome to your account"
# compare age with userAge

# if the age is greater than 18, print "You are allowed to withdraw"
# else print "You are not allowed to withdraw"
# if the age is greater than 100, you are supposed to be dead

# TASK SOLUTION

pin = 1234
userPin = 1234  
userAge = 25   

if pin == userPin:
    print("Welcome to your account")

    if userAge > 18:
        print("You are allowed to withdraw")
    elif userAge > 100:
        print("You are supposed to be dead")
    else:
        print("You are not allowed to withdraw")
else:
    print("Your PIN is incorrect. Kindly try again!")
