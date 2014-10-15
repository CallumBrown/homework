#Callum Brown
#Task 6 iteration




message = input("Please enter a message: ")
time =int(input("Please enter the amount of times you would like it to be repeated: "))

while time > 0:
    print(message)
    time = time-1




password = input("Please enter a password: ")
while password != 'secret':
    print("Please try again")
    password = input("Please enter the password: ")
print("You can now login")
