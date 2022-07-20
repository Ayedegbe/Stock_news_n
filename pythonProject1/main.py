Height= int(input('''Welcome to chucky cheese roller coaster ride,
How tall are you ?'''))
bill = 0
if Height >= 120:
    print("Congratulations!!!, you are tall enough for this ride.")
    age =int(input("How old are you?"))
    if age <= 12:
        bill = 5
        print('Child ticket is $5')
    if 45 < age < 55:
        bill = 0
        print(f"You get to ride free.")

    elif age <=18:
        bill = 7
        print("Youth ticket $7.")
    else:
        bill = 12
        print("Adult ticket is $12.")
    wantsphoto = input("Do you want photo? type y for yes and N for no: ")
    if wantsphoto == "y" or  wantsphoto == "Y":
        bill += 3
        print (f"your final bill is {bill}")
    else:
        print(f'Your final bill is {bill}')
else:
    print("You're too short for this ride.")
