import random
import words
import art
print(art.logo)
chosen_word =  random.choice(words.word_list)
display = []
word_length = len(chosen_word)
end_of_game = False
life = 6
for _ in range(word_length):
    display+= "_"
while not end_of_game:
    print(display)
    guess = input("Guess a letter").lower()
    if guess in display:
        print(f"You have guessed this letter {guess}")
    for n in range(word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter
    if "_" not in display:
        end_of_game = True
        print("You win")
    if guess not in chosen_word:
        life -=1
        print(art.stages[life])
        print(f"{guess} is not in the options try another ")
    if life == 0:
        end_of_game = True
        print(f"Game over!!! you have {life} life")