import random

def Rock_Paper_Scissors():
    options = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Rock, Paper, or Scissors?\n").lower()  
        if player_choice not in options:
            print("You've entered the wrong input!")
            continue

        computer_choice = random.choice(options)
        print(f"Computer's choice was: {computer_choice}")

        if computer_choice == player_choice:
            print("You tied with the computer!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("Hoorayyyy!!! You Won!!")
        else:
            print("Sorry, you lost!")

        replay = input("Do you want to play another game? (y/n): ").lower()
        if replay != "y":
            print("Hope you enjoyed :)")
            break

Rock_Paper_Scissors()
