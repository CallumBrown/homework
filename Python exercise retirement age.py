#Callum Brown
#25-09-14
#Retirement age


age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You aren't old enough to vote")

retirement_age = (65-age)

print("You can retire in {0} years".format(retirement_age))

    
