"""
PROGRAMMER: William Griffin
DATE: Feb. 02, 2019
ASSIGNMENT: Number #2
ALGORITHM: This program allows users to play or quit upon start. Once started the user will roll the first round and either win, lose, or roll again,
on second roll the user will either win or lose if they roll on the number 7. After a win or loss the user will have the option to play again.
"""

import sys
import random


def dice():
    """ This function rolls two dice and returns them"""
    dice_roll = random.randint(1, 6) + random.randint(1, 6)
    return dice_roll


def replay():
    """ This function asks the user if they would like to play again taking a 'y' or 'n' answer."""
    play_again = input("Would you like to play again?\nyes(y) / no(n)\n: ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    elif play_again.lower() == 'y':
        play()
    else:
        print("Sorry, I don't understand that input, starting game over...\n")
        main()


def play():
    """ This function is used for the initial roll. The player wins if they roll 7 or 11, looses if they roll 2, 3,
    or 12. If the player rolls a point if they roll another number. """
    global rolls
    roll_dice = input("Press ENTER to roll")
    rolls = dice()
    if rolls in [7, 11]:
        print("You rolled {}, you win".format(rolls))
        replay()
    elif rolls in [2, 3, 12]:
        print("You rolled {} craps, you lose\n".format(rolls))
        replay()
    else:
        print("Point. You rolled {}".format(rolls))
        re_roll()


def re_roll():
    """ This function is used for the point. If the user rolls a 7 they lose, otherwise the function continues until
    the player either lands on 7 or on their point number. """
    roll_dice = input("Press ENTER to roll")
    roll2 = dice()
    if roll2 == rolls:
        print("You rolled {} again, you win!\n".format(roll2))
        replay()
    elif roll2 == 7:
        print("You rolled {}, you lose".format(roll2))
        replay()
    else:
        print("You rolled {}".format(roll2))
        re_roll()


def main():
    """ This function is the main function, It welcomes the user, and gives the user a choice to either play or quit.
    If the user types an invalid input the game exits. """
    while True:
        welcome = "Welcome to the craps table!"
        print("=" * len(welcome))
        print(welcome)
        print("=" * len(welcome))
        start_game = input("To Play press (r)\nto Quit press (q)\n: ")
        if start_game.lower() == 'q':
            print("Thanks for playing!")
            sys.exit()
        elif start_game.lower() == 'r':
            print("Let's play!")
            play()
        else:
            print("Sorry, you typed the wrong answer exiting game...")
            sys.exit()


if __name__ == '__main__':
    main()
