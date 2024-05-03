# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import shark
import random
import re

def username():
    """
    The function provides a option for the user to create there name. 
    This will use regular expresstion to validate ther user name using only letters with a length 1<15.
    Will print error when false. 
    """
    while True:
        user_name = input("Ahoy there, matey! What might be your handle?\n ")
        if 1 <= len(user_name) <=15 and re.fullmatch(r'^[A-Za-z]+$', user_name):
            return user_name
        else:
            print(f"{user_name}, ye scallywag! Yer handle should be naught but letters, from A to Z, both upper and lower,\n and be no shorter than a single letter and no longer than fifteen,\n with no other scurvy characters like numbers or symbols or the like!")
            break 


def main():
    """
    To call all other functions in the game.
    """
    shark.welcome_msg()
    username()

main()


