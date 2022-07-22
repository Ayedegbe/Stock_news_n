def spin_words(sentence):
    see = sentence.split()
    return " ".join([[char::-1] if len(char) > 4 else char for char in see])