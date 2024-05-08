# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import shark
import random
import re


def username():
    """
    The function provides a option for the user to create there name. 
    This will use regular exprestion to validate ther user name using only letters with a length 1<15.
    Will print error when false and when True will print start msg. 
    """
    while True:
        user_name = input("Ahoy there, matey! What might be your handle?\nA handle has letters only from 1 to 15 letters.\n ")
              
        if 1 <= len(user_name) <=15 and re.fullmatch(r'^[A-Za-z]+$', user_name):
            print(shark.correct_name(user_name))
            return user_name
           
        else:
            print(shark.incorrect_name(user_name))
            
def gamerules(user_name):
    """
    To provide and option for the user to see the game rules.
    """
    while True:
        game_rules = input(f"{user_name}! Should ye want to see the rules, press Y or N or E to exit, savvy?\n" )
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
            print(shark.exit_msg(user_name))
            exit()
           


def random_word():
    """
    This will return a random word from the word list in shark file.
    """
    return random.choice(shark.words).lower()


def guess_word_letter(word):
    """
    For the user to guess the a single letter .
    """
    letter_pattern = r'^[a-z]$'
    lives = 0
    max_lives = 6
    guessed_letters = set()
    guess_wrong = []
    guess_correct = []
    letter_word = ['_'] * len(word)
    
    print(word) #remove later for testing
    while True:
        print("_".join(letter_word))
        guess_letter = input("Guess a letter: ").lower()

        while not re.match(letter_pattern, guess_letter) or guess_letter in guessed_letters:
            if not re.match(letter_pattern, guess_letter):
                print("Foul value, use alphabet letters only!")
                break
                
        
            elif guess_letter in guessed_letters:
                print("Struck a dud, already used pick a fresh letter!")
                break

        guessed_letters.add(guess_letter)
        
        print(guessed_letters) # remove later this is for testing    
        # enumerate() method to iterate over char with i stores, index. 
        if re.match(letter_pattern, guess_letter):
            print(f"Aye, that's correct: {guess_letter}")
            for i, char in enumerate(word):
                if char == guess_letter:
                    letter_word[i] = guess_letter
                    
                    
        else:
            print(f"Nay, matey: {guess_letter}")
            
        if "_" not in letter_word:
            #creat image later 
            print(f"Splendid catch, me hearty! Bravo, well won!\n Your correctly guessed word is {word}" )
            break    
   

# def game_run():
    """
    This will be the main function.
    Provide information as to lives left and art graphics view.
    User will guess the letters until completed or until life has been depleted.
    """

    

 
def main():
    """
    To call all other functions in the game
    """
    #shark.welcome_msg()
    #name = username()
    #gamerules(name)
    word = random_word()
    guess_word_letter(word) 
   
    
    

   
    
main()


