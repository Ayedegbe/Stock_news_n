import random
bankers = input("Input participants name seperated by a ,")
names = bankers.split(" ")
number = (len(names))
payer = random.randint(0, number-1)
payer = names[payer]
print(f'{payer} is due to pay')