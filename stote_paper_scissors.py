import random

options = ("rock", "scissors", "paper")
running = True

while running:
    player = None

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a TIE!!!")

    elif (player == "paper" and computer == "rock") or \
            (player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper"):
        print("You WIN!!!")

    else:
        print("!!!!! You LOSE !!!!!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False

print("Thanks for playing!")
