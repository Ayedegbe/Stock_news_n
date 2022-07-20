height = float(input("How tall are you in meters?: "))
weight = float(input("What do you weigh?: "))
BMI = round(weight / height**2)
if BMI < 18.5:
    print (f"Your BMI is {BMI} you are underweight")
elif BMI <=25:
    print(f"Your BMI is {BMI} You have normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}You have slightly overweight.")
elif BMI <=35:
    print(f"Your BMI is {BMI} You are Obese.")
else:
    print(f"Your BMI is {BMI} You are clinically obese.")