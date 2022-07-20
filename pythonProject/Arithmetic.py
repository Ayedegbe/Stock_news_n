price =input("Total cost of goods: ")
tip = input("% Tip 10 12 or 15 percent : ")
split = input("Split between how many people?  : ")
split = int(split)
price = float(price)
tip = int(tip)
amount =round (price + (tip / 100 * price),2)
ZZZ = (amount/split)
print(f"The total amount is {amount}$.\n With tip of {tip}% split between 5 people, \n Each person is to pay {ZZZ}$ ")



