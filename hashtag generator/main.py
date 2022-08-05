#hashtag generator
key = "#"
word = "MWbKkYDnGIb pELFJukxwqp PA R uHnOma DbCL LoFZop xQyBsdncKZA MWxRWVucmVy A EFptcoDMy RRMBajnUGgg"
def hashtag_generator(word):
    word = word.lower()
    words = word.split()
    words.insert(0, key)
    breed = []
    for n in words:
        if n[0].islower():
            #print(n)
            n = n.replace(n[0], n[0].upper())
        breed.append(n)
        worded = "".join(breed)
    if len(worded) > 140 or word == " ":
        return False
    else:
        return worded

print(hashtag_generator(word))
