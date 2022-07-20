import random
import art
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_score(user_score,computer_score):
    if user_score > 21:
        return "Your opponent has won"
    if computer_score > 21:
        return "You have won"
    if user_score == computer_score:
        return "It is a draw"
    if user_score > 21 and computer_score > 21:
        return "You both went over , you both loose"
    elif user_score == 21:
       return "You win with a blackjack"
    elif computer_score == 21:
        return "Computer wins with a blackjack"
def play_blackjack():
    global computer_score
    print(art.logo)
    user_card = []
    computer_card = []
    still_on = True
    for s in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while still_on:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"User cards are {user_card} and user score is {user_score}")
        print(f"Computer cards are {computer_card[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            still_on = False
        else:
            deal_more = input("Do you want another card? type y for yes and n for no ")
            if deal_more == "y":
                user_card.append(deal_card())
            else:
                still_on = False
    if computer_score != 0 or computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your final hand is {user_card} and your final score is {user_score}")
    print(f"Computer final hand is {computer_card} and final score is {computer_score}")
    print(compare_score(user_score, computer_score))
while input("Would you like to play a game of black jack? type y for yes and n for no ") == "y":
    play_blackjack()
else:
    print("Bye bitch")
