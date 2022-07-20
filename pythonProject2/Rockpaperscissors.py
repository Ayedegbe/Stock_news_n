import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = input("What is your choice? type 0 for rock , 1 for paper , 2 for scissors\n")
options = [rock, paper, scissors]
option = len(options)
computer_choice = random.randint(0, option-1)
computer_choice = options[computer_choice]
print(f'computer chose\n{computer_choice}')
player_choice = int(player_choice)
player_choice = options[player_choice]
print(f' player chose\n {player_choice}')
if player_choice == rock and computer_choice == rock or player_choice == paper and computer_choice == paper or player_choice == scissors and computer_choice == scissors:
    print("It is a draw")
else:
    if player_choice == rock and computer_choice == paper:
        print("paper beats rock.\n Computer wins ")
    elif player_choice == paper and computer_choice == rock:
        print("rock looses to paper,player wins")
    elif player_choice == rock and computer_choice == scissors:
        print("Rock beats scissors, player wins")
    elif player_choice == scissors and computer_choice == rock:
        print("Scissors looses to rock, computer wins")
    elif player_choice == scissors and computer_choice == paper:
        print("Scisors beats paper, player wins")
    else:
        print("paper looses to scissors, computer wins")
