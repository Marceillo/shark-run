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
    Will print error when false and when True will print start msg. 
    """
    while True:
        user_name = input("Ahoy there, matey! What might be your handle?\nA handle has letters only from 1 to 15 letters.\n ")
              
        if 1 <= len(user_name) <=15 and re.fullmatch(r'^[A-Za-z]+$', user_name):
            print(shark.correct_name(user_name))
            return user_name
           
        else:
            print(f"{user_name}, ye scallywag! Yer handle should be naught but letters, from A to Z, both upper and lower,\n and be no shorter than a single letter and no longer than fifteen,\n with no other scurvy characters like numbers or symbols or the like!")
            break 
def gamerules(user_name):
    """
    To provide and option for the user to see the game rules.
    """
    while True:
        game_rules = input(f"{user_name}! Should ye want to see the rules, press Y or N or E to exit, savvy?" )
        if re.fullmatch(r'[YyNnEe]', game_rules):
            game_rules = game_rules.lower()
        if game_rules == 'y':
            print()
            shark.instructions()
            break
            
        elif game_rules == 'n':
            print(f"{user_name} Alright, ye scallywags! Let's be shovin' off, shall we?")
            break
        elif game_rules == 'e':
            print(f"{user_name}! Arr, ye scallywags, it pains me heart to see ye shove off.But take heart, for I know ye'll be back to join us once more, aye?")
            break


def random_word(words):
    """
    This will return a random word from the word list in shark file.
    """
    return random.choice(words)



    
  


        

def main():
    """
    To call all other functions in the game.
    """
    shark.welcome_msg()
    name = username()    
    gamerules(name)
    

   
    
main()


