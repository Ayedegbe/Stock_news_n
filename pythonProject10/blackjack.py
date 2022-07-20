import random
import art

def deal():
    start_card = random.sample(card, k=2)
    computer_cards =random.sample(card, k=1)
    score = sum(start_card)
    c_score = sum(computer_cards)
    #print(f"Your cards are {start_card}\n your score is {score}")
    #print(f"Computer card is {computer_cards} and the score is{c_score}")
    while still_on:
        if score == 21 or c_score ==21:
            
        draw_card = input("Draw another card")
        if draw_card == "y" and score < 21 and c_score < 21:
            start_card += random.sample(card, k=1)
            computer_cards += random.sample(card, k=1)
            score = sum(start_card)
            c_score = sum(computer_cards)
            print(f"Your cards are {start_card}\n your score is {score}")


print(art.logo)
play_blackjack = input("Do you want to play black jack? type y for yes and n for No: ")
if play_blackjack == "y":
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    still_on = True
    deal()











