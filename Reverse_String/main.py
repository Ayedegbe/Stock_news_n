def reverse(text):
    see = text.split()
    y = []
    print(see)
    for char in see:
        if len(char) > 4:
           # print(char)
            big = text.replace(char, char[::-1])
           # print(y)
            return big

green = "Whose is ronaldinho"
print(reverse(green))