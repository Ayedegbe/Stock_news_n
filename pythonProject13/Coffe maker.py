import MENU
import os


def clear():
    os.system('cls')


still_on = True
espresso = MENU.MENU["espresso"]
cappuccino = MENU.MENU["cappuccino"]
latte = MENU.MENU["latte"]
resource = {"water": MENU.resources["water"], "milk": MENU.resources["milk"], "coffee": MENU.resources["coffee"]}
profit = 0


def check_amount(order):
    price = order["cost"]
    notes = int(input("How many dollars you fitting in the machine: "))
    coins = float(input("How many coins: "))
    amount = notes + coins
    difference = abs(price - amount)
    if amount < price:
        print(f"You haven't paid enough you need to pay {difference}$ extra to get your beverage")
        extra = int(input("How much coins added?: "))
        amount = notes + coins + extra
        print("Your beverage is on the way")
        return True
    elif amount > price:
        print(f"You have over paid and your change is {difference}$")
        print("Your beverage is on the way")
        return True
    else:
        print(f'Thank you for your order, we are making your beverage, give us a minute')
        return True


def check_ingredient(order, contents):
    order = order["ingredients"]
    for items in order:
        if order[items] > contents[items]:
            print(f'Insufficient {items}')
            return False
    else:
        return True


def make_coffee(order, features):
    ingredient = order["ingredients"]
    for items in ingredient:
        features[items] -= ingredient[items]
    print(f"Here is your beverage ☕️")


def play_game():
    global profit
    while still_on:
        preference = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if preference == 'espresso':
            order = espresso
        elif preference == 'cappuccino':
            order = cappuccino
        elif preference == 'latte':
            order = latte
        else:
            print('Select a valid option or leave the QUEUE')
        check_ingredient(order, resource)
        if check_ingredient(order, resource):
            if check_amount(order):
                make_coffee(order, resource)
                profit += order['cost']
                print(profit)

        clear()
play_game()