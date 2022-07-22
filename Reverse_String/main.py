def reverse(text):
    see = text.split(" ")
    return " ".join([char[::-1] if len(char) >=5 else char for char in see])


green = "Hey fellow warriors"
print(reverse("This is another test"))
