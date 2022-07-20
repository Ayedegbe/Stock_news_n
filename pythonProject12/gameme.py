import main
import random
import art
game_start = False
#select two numbers at random and pick their respective dictinoaries
two_numbers = random.sample(range(0,51),2)
first_dict = main.data[two_numbers[0]]
second_dict = main.data[two_numbers[1]]
follower1 = first_dict["follower_count"]
follower2 = second_dict["follower_count"]
print(f"""Compare A: {first_dict['name']} a {first_dict['description']} from {first_dict['country']}
{art.logo2} 
Compare B: {second_dict['name']} a {second_dict['description']} from {second_dict['country']}""")

def compare_followers(number_1=two_numbers[0],number_2=two_numbers[1]):
    follower1 =main.data[number_1["follower_count"]]
    follower2 =main.data[number_2["follower_count"]]
    print(follower1)
    print(follower2)
def play_game():
    print("Welcome to FOLLOWERS GUESSING GAME")
    print(art.logo)
    should_start = input("Would you like to begin? type in y for yes and n for no: ")
    if should_start == "y":
        #game_start == True
        #players()
        compare_followers()


        #get_followers(first_dict,second_dict)

        #answer = input("Who has more followers? A or B")


play_game()

    #print(f"The first player is {first_dict['name']} and is a {first_dict['description']} from {first_dict['country']} and second player is {second_dict['name']} and is a {second_dict['description']} from {second_dict['country']}")
    #choice = input("Which of this persons have more followers? A or B (A for player 1 and B for player 2")
    #if choice == "A":
     #   answer = int(follower1)
    #else:
     #   answer= int(follower2)




#print(main.data[1]['name'])
