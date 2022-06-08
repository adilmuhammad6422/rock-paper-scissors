#first self project
#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⠛⢩⣴⣶⣶⣶⣌⠙⠫⠛⢋⣭⣤⣤⣤⣤⡙⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⡟⢡⣾⣿⠿⣛⣛⣛⣛⣛⡳⠆⢻⣿⣿⣿⠿⠿⠷⡌⠻⣿⣿⣿⣿
#⣿⣿⣿⣿⠏⣰⣿⣿⣴⣿⣿⣿⡿⠟⠛⠛⠒⠄⢶⣶⣶⣾⡿⠶⠒⠲⠌⢻⣿⣿
#⣿⣿⠏⣡⢨⣝⡻⠿⣿⢛⣩⡵⠞⡫⠭⠭⣭⠭⠤⠈⠭⠒⣒⠩⠭⠭⣍⠒⠈⠛
#⡿⢁⣾⣿⣸⣿⣿⣷⣬⡉⠁⠄⠁⠄⠄⠄⠄⠄⠄⠄⣶⠄⠄⠄⠄⠄⠄⠄⠄⢀
#⢡⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣿⣦⣤⣀⣀⣀⣀⠄⣤⣾
#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⡶⢇⣰⣿⣿⣟⠿⠿⠿⠿⠟⠁⣾⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⡟⢛⡛⠿⠿⣿⣧⣶⣶⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣧⠸⣿⣿
#⠘⢿⣿⣿⣿⣿⣿⡇⢿⡿⠿⠦⣤⣈⣙⡛⠿⠿⠿⣿⣿⣿⣿⠿⠿⠟⠛⡀⢻⣿
#⠄⠄⠉⠻⢿⣿⣿⣷⣬⣙⠳⠶⢶⣤⣍⣙⡛⠓⠒⠶⠶⠶⠶⠖⢒⣛⣛⠁⣾⣿
#⠄⠄⠄⠄⠄⠈⠛⠛⠿⠿⣿⣷⣤⣤⣈⣉⣛⣛⣛⡛⠛⠛⠿⠿⠿⠟⢋⣼⣿⣿
#⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⣻⣿⣿⣿⣿⡿⠿⠛⠃⠄⠙⠛⠿⢿⣿
#⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢬⣭⣭⡶⠖⣢⣦⣀⠄⠄⠄⠄⢀⣤⣾⣿
#⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⠄⢠⣾⣿⣿⣿

import random
user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

print("Welcome to Rock paper scissors!" "\n")

while True:
    random_number = random.randint(0,2)
    computer = options[random_number]

    user_input = input("Type rock, paper, scissors or quit:" "\n").lower()
    
    if user_input == "quit":
        print("Sad to see you go")
        break

    if user_input not in options:
        print("If you typed something else, please use rock paper or scissors")
        print("please run it again""\n")
        break

    print("Great choice!, heres what I picked:", computer)

#if user wins
    if user_input == "rock" and computer == "scissors":
        user_wins += 1
        print("Damn. You won")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "paper" and computer == "rock":
        user_wins += 1
        print("Damn. You won")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue    

    elif user_input == "scissors" and computer == "paper":
        user_wins += 1
        print("Damn. You won")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

#if computer wins
    if user_input == "scissors" and computer == "rock":
        computer_wins += 1
        print("YOU LOST")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "rock" and computer == "paper":
        computer_wins += 1
        print("YOU LOST")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue    

    elif user_input == "paper" and computer == "scissors":
        computer_wins += 1
        print("YOU LOST")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

#if they draw
    if user_input == "scissors" and computer == "scissors":
        print("Draw")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "rock" and computer == "rock":
        print("Draw")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue    

    elif user_input == "paper" and computer == "paper":
        print("Draw")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue







    

