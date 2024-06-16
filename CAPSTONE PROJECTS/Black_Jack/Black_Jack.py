#Black_Jack

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Cards available
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# Calculate the sum of cards in hand
def add(card):
    total = 0
    aces = 0
    for i in card:
        if isinstance(i, int):
            total += i
        elif i in ["K", "Q", "J"]:
            total += 10
        elif i == "A":
            aces += 1
            total += 11
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Computer play of cards in hand
def comp_play(comp):
    while add(comp) < 17:
        comp.append(random.choice(cards))
    return add(comp)

# Playing the game
def check(player, comp, ap, ac):
    print(f"Your cards: {player}, current score: {ap}")
    print(f"Computer's first card: {comp[0]}")
    if ap == 21:
        print("You have Blackjack! You Win!! :)")
        return "n", True
    elif ac == 21:
        print("Computer has Blackjack! You lose!! :(")
        return "n", True
    else:
        return input("Do you want another card? Type 'y' or 'n': "), False

#game starts
print(logo)
option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

#game
while option != 'n':
    player = random.sample(cards, 2)
    comp = random.sample(cards, 2)
    ap = add(player)
    ac = add(comp)
    game_over = False

    #player game
    while option == 'y' and not game_over:
        option, game_over = check(player, comp, ap, ac)
        if option == 'y':
            player.append(random.choice(cards))
            ap = add(player)
            if ap > 21:
                print(f"Your final cards: {player}, final score: {ap}")
                print("You went over 21! You lose!! :(")
                game_over = True
                option = 'n'

    #computer game
    if not game_over:
        ac = comp_play(comp)
        print(f"Computer's final cards: {comp}, final score: {ac}")
        if ac > 21 or ap > ac:
            print("You Win!! :)")
        elif ap < ac <= 21:
            print("You lose!! :(")
        else:
            print("It's a draw!!")

    #new game
    option = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")

print("Thanks for playing!")
