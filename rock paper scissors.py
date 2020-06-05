# Regina's shabby code for rock, paper, scissors :)
# I welcome any and all feedback

import random

# options for the game
choices = ("rock", "paper", "scissors")

# logic for the game
def who_won(choice, comp_choice, user_choice):
    if comp_choice == user_choice:
        print("It's a tie!")
    else:
        if comp_choice == "rock" and user_choice == "paper":
            print("You won!")
        elif comp_choice == "rock" and user_choice == "scissors":
            print("You lost. :(")
        elif comp_choice == "paper" and user_choice == "scissors":
            print("You won!")
        elif comp_choice == "paper" and user_choice == "rock":
            print("You lost. :(")
        elif comp_choice == "scissors" and user_choice == "rock":
            print("You won!")
        elif comp_choice == "scissors" and user_choice == "paper":
            print("You lost. :(")
        print("The computer's choice is: ", comp_choice)

# this is where the computer makes its choices and the user selects theirs.
# there's some validation to make sure the user enters a valid option.
# user options are converted to lower so it's comparable with the choices tuple.
def main():
    global choices
    comp_rps = random.choice(choices)
    user_rps = input("rock, paper or scissors?\n").lower()
    while user_rps not in choices:
        user_rps = input("please enter either 'rock', 'paper' or 'scissors'\n").lower()
    who_won(choices, comp_rps, user_rps)

main()
