import random
direction = ("n", "s", "w" "e")
distance = random.randint(1,15)
direct = []
for n in range(distance):
    direct.append(random.choice(direction))
def walk(direct):
    x = 0
    y = 0
    for items in direct:
        if items == "n":
            x += 1
        if items == "s":
            x -= 1
        if items == "e":
            y += 1
        if items == "w":
            y -= 1
    if x == 0 and y == 0 and len(direct) == 10:
        return True
    else:
        return False
print(walk(direct))