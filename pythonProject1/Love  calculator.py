name = input("What is your name? \n")
Name = input("What is your spouses name \n")
name = name.lower()
Name = Name.lower()
Total = name + Name
t = Total.count("t")
r = Total.count("r")
u = Total.count("u")
e = Total.count("e")
l = Total.count("l")
o = Total.count("o")
v = Total.count("v")
e = Total.count("e")
true = str(t+r+u+e)
love = str(l+o+v+e)
lovescore = true + love
lovescore = int(lovescore)
print(lovescore)
if lovescore < 10 or lovescore > 90:
    print(f'Your love score is {lovescore}, you go together like coke and mentos')
elif lovescore > 10 or lovescore < 90:
    print(f'Your lovescore is {lovescore}, you are alright together.')
else:
    print(f'Your love score is {lovescore}')
