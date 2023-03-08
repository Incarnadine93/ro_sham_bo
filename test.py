import random

print("--------Rock, paper scissors. Best of 3--------")
player = 0
enemy = 0

while True:
    player_roll = input(f'R for Rock, P for paper, S for scissors, or Q to quit: ') 
    confirm = player_roll[0].lower() 
    if player_roll == '' or not confirm in ['r','p','s','q']: 
        print('Please answer with r, p, s or q! ')
    if player_roll == '' or confirm in ['q']:
        if player > enemy: # if player reaches win parameter and outputs victor
            print("Thank you for playing")
            print("You've won this battle. Somehow")
            print(f"Player points: {player}          Bot points: {enemy}")
        elif enemy > player: # if enemy reaches win parameter and outputs victor
            print("Thank you for playing")
            print("You've lost this battle. Scum")
            print(f"Player points: {player}          Bot points: {enemy}")
        elif enemy == player: # if tie parameter is reached and outputs victor
            print("Thank you for playing")
            print("We've tied. Unfortunately")
            print(f"Player points: {player}          Bot points: {enemy}")
        break
    possible_actions = ["r", "p", "s"]
    enemy_roll = random.choice(possible_actions)
    if player_roll == enemy_roll:
        print("Game Tied")
    else:
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