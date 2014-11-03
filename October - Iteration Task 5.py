#Callum Brown
#October half term
#Iteration exercise 7

number = int(input("How many starts would you like in each row? "))
rows = int(input("How many rows would you like? "))
list1=''
for count in range(number):
    list1= list1 + '*'
for count in range(rows):
           print(list1)
