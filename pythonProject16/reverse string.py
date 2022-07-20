import re
newData = "GeeksforGeeks, is_an-awesome ! app + too"
sentence =  "Where is Ronaldinho"

# To split "+" use backslash
sentence = re.split(' ', sentence)
for  char in sentence:
    if len(char) >= 5:
        sentence.append(char[::-1])
print(sentence)




