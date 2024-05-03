# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import shark
import random

def username():
    user_name = input("Ahoy there, matey! What might be your handle?\n ")


def main():
    """
    To call all other functions in the game.
    """
    shark.welcome_msg()
    username()

main()


