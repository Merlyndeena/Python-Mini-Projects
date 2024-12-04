# from enum import IntEnum
# import random
# class various_action(IntEnum):
#     rock=0
#     paper=1
#     scissors=2
# def get_user_selection():
#     choices = [f"{act.name}[{act.value}]" for act in various_action]
#     choices_string = ",".join(choices)
#     selection = int(input(f"Enter a choice ({choices_string}): "))
#     act = various_action(selection)
#     return act
#
# def get_computer_selection():
#     selection = random.randint(0,len(various_action)-1)
#     act = various_action(selection)
#     return act
#
#
# def determine_winner(user_selection,computer_selection):
#
#     if user_selection == computer_selection:
#         print("Its a tie..!")
#     elif user_selection == various_action.rock:
#         if computer_selection == various_action.paper:
#             print("paper covers rock,you lose...!")
#         else:
#             print("rock smashes scissors....You win")
#     elif user_selection == various_action.paper:
#         if computer_selection == various_action.rock:
#             print("paper covers rock....you win")
#         else:
#             print("scissors cuts paper....you loose")
#     elif user_selection == various_action.scissors:
#         if computer_selection == various_action.rock:
#             print("rocks smashes scissors...You loose")
#         else:
#             print("scissors cuts paper...you win")
#
# while True:
#     user_selection= get_user_selection()
#     computer_selection=get_computer_selection()
#     determine_winner(user_selection,computer_selection)
#     play_again=input("Play again? (y/n)")
#     if play_again.lower() != "y":
#         break
#
#

from enum import IntEnum
import random

class VariousAction(IntEnum):  # Class names should be in CamelCase
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def get_user_selection():
    choices = [f"{act.name}[{act.value}]" for act in VariousAction]
    choices_string = ",".join(choices)
    while True:
        try:
            selection = int(input(f"Enter a choice ({choices_string}): "))
            act = VariousAction(selection)
            return act
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")
        except KeyError:
            print("Invalid choice. Please select a valid option.")

def get_computer_selection():
    selection = random.randint(0, len(VariousAction) - 1)
    act = VariousAction(selection)
    return act

def determine_winner(user_selection, computer_selection):
    if user_selection == computer_selection:
        print("It's a tie!")
    elif user_selection == VariousAction.ROCK:
        if computer_selection == VariousAction.PAPER:
            print("Paper covers rock, you lose!")
        else:
            print("Rock smashes scissors, you win!")
    elif user_selection == VariousAction.PAPER:
        if computer_selection == VariousAction.ROCK:
            print("Paper covers rock, you win!")
        else:
            print("Scissors cuts paper, you lose!")
    elif user_selection == VariousAction.SCISSORS:
        if computer_selection == VariousAction.ROCK:
            print("Rock smashes scissors, you lose!")
        else:
            print("Scissors cuts paper, you win!")

while True:
    user_selection = get_user_selection()
    computer_selection = get_computer_selection()
    determine_winner(user_selection, computer_selection)
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

