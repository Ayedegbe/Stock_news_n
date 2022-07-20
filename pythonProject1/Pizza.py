print('Welcome to python pizza ')
size = input("What size of pizza do you want? S, M, L ")
pepperoni = input("Do you want pepperoni on your pizza? Y/N ")
cheese = input("Extra cheese? Y/N ")
bill = 0
if size == "S" or size == "s" :
    bill = 15
    if pepperoni == "Y" or pepperoni == "y":
        bill += 2
    if cheese == "Y" or cheese == "y":
         bill += 1
         print(f"Your bill is {bill} with pepperoni and cheese")
    else:
        print(f'Your bill is  {bill} without pepperoni and cheese')
elif size == "M" or size == "m" :
    bill = 20
    if pepperoni == "Y" or pepperoni == "y":
        bill += 2
    if cheese == "Y" or cheese == "y":
        bill += 1
        print(f"Your bill is {bill} with pepperoni and cheese")
    else:
        print(f'Your bill is  {bill} without pepperoni and cheese')
else:
    bill = 25
    if pepperoni == "Y" or pepperoni == "y":
        bill += 2
    if cheese == "Y" or cheese == "y":
        bill += 1
        print(f"Your bill is {bill} with pepperoni and cheese")
    else:
        print(f'Your bill is  {bill} without pepperoni and cheese')