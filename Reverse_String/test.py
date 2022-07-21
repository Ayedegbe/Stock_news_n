def spin_words(sentence):
    sentence = sentence.split()
    word = [word for word in sentence if len(word) >= 5]
    reversed = [reverse[::-1] for reverse in word]
    sentencee = sentence.replace(word, reversed)
    return sentencee

print(spin_words("This Awesome testly"))