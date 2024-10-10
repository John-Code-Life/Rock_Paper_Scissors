"""Game rock, paper, scissors with an etra features"""

import random


# Read the initial ratings from the file
def get_user_rating(username):
    """Takes username and returns score"""
    with open("rating.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            name, score = line.split()
            if name == username:
                return int(score)
    return 0


# Update the rating in the file
def update_user_rating(username, score):
    """Updates user rating"""
    updated = False
    lines = []
    with open("rating.txt", mode="r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("rating.txt", mode="w", encoding="utf-8") as file:
        for line in lines:
            name, current_score = line.split()
            if name == username:
                file.write(f"{name} {score}\n")
                updated = True
            else:
                file.write(line)
        if not updated:
            file.write(f"{username} {score}\n")


# Determine the result based on the game rules
def get_result(user_choice, computer_choice, options):
    """Takes shape as an input and returns he win or lose result"""
    if user_choice == computer_choice:
        return "draw"
    user_index = options.index(user_choice)
    beats = options[user_index + 1 :] + options[:user_index]
    half_length = len(beats) // 2
    if computer_choice in beats[:half_length]:
        return "lose"
    return "win"


# Main game logic
def play_game():
    """This one makes all the hard work done"""
    name = input("Enter your name: ")
    print(f"Hello, {name}")

    # Get user's starting score from rating.txt
    score = get_user_rating(name)

    # Get the game options
    user_options = input().split(",")
    if not user_options[0]:  # If the user inputs an empty line, use the default options
        user_options = ["rock", "paper", "scissors"]

    print("Okay, let's start")

    # Play the game
    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye!")
            update_user_rating(name, score)
            break
        elif user_input == "!rating":
            print(f"Your rating: {score}")
        elif user_input in user_options:
            computer_choice = random.choice(user_options)
            result = get_result(user_input, computer_choice, user_options)

            if result == "draw":
                print(f"There is a draw ({computer_choice})")
                score += 50
            elif result == "win":
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input")


# Entry point to run the game
if __name__ == "__main__":
    play_game()
