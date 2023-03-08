#For Brandt
# When I change line 11 to "and" instead of or then the code works and breaks when either player hits the value of 2
# I can get the code to work with a while true loop and while "___ and ___". Just trying to see how to get the "while ___ or ___" to work

import random

print("--------Rock, paper scissors. Best out of 3--------") #initial statement
player = 0 # assigning win value to player
enemy = 0 # assigning win value to enemy

while player != 2 or enemy != 2: # loop that breaks when either reach 2 points. BUT its not breaking
    while True: # while true loop to confirm player input is valid
        player_roll = input(f'R for Rock, P for paper, or S for scissors? ') # taking in user input for game
        confirm = player_roll[0].lower() # Assigning value of player input
        if player_roll == '' or not confirm in ['r','p','s']: # if player input is invalid
            print('My guy. The options r, p, or s!') # Output reminding player of possible inputs
        else: # if player input is valid
            break
    possible_actions = ["r", "p", "s"] # list of enemy's actions
    enemy_roll = random.choice(possible_actions) # Randomizing enemy's action and assigning value to enemy_roll
    if player_roll == enemy_roll: # if both selections match
        print("Game Tied")
    else: # Outputting who won and incrementing their respective count
        if player_roll.lower() == "r" and enemy_roll == "s":
            print("You win")
            player += 1
        elif player_roll.lower() == "r" and enemy_roll == "p":
            print("You lose")
            enemy += 1
        elif player_roll.lower() == "p" and enemy_roll == "s":
            print("You lose")
            enemy += 1  
        elif player_roll.lower() == "p" and enemy_roll == "r":
            print("You win")
            player += 1  
        elif player_roll.lower() == "s" and enemy_roll == "r":
            print("You lose")
            enemy += 1  
        elif player_roll.lower() == "s" and enemy_roll == "p":
            print("You win")
            player += 1 
    if player == 2: # if player reaches win parameter and outputs victor
        print("You've won this battle. Somehow")
    elif enemy ==2: # if enemy reaches win parameter and outputs victor
        print("You've lost this battle. Scum")