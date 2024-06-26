import shark
import random
import re
import time


def username():
    """
    The function provides a option for the user to create username.
    This will use regular exprestion to validate the username.
    Using only letters with a length 1 to 15.
    Will print a error when false and when True will print a message.
    """
    while True:
        print()
        user_name = input("Ahoy there, matey! What might be your handle?\n"
                          "A handle has letters only from 1 to 15 letters.\n")
        if 1 <= len(user_name) <= 15 and \
           re.fullmatch(r'^[A-Za-z]+$', user_name):
            print(shark.correct_name(user_name))
            return user_name
        else:
            shark.clear_screen()
            print(shark.incorrect_name(user_name))


def gamerules(name):
    """
    To ask the user the user if they would like to see the rules.
    If yes to print the rules to the consol.
    """
    while True:
        game_rules = input(f"{name}! Should ye want to see the rules:\n"
                           "Y too see rules.\n"
                           "N not too see the rules and start the game.\n"
                           "E too exit, savvy?\n")
        if re.fullmatch(r'[YyNnEe]', game_rules):
            game_rules = game_rules.lower()
        if game_rules == 'y':
            shark.clear_screen()
            shark.instructions()
            continue
        elif game_rules == 'n':
            print(f"{name} Alright, ye scallywags!\n"
                  "Let's be shovin' off, shall we?")
            time.sleep(4)
            shark.clear_screen()
            break
        elif game_rules == 'e':
            shark.clear_screen()
            shark.exit_msg(name)
            exit()


def random_word():
    """
    This will return a random word from the word list in shark file.
    """
    return random.choice(shark.words).lower()


def guess_word_letter(name, guessed_letters):
    """
    For the user to guess the a single letter.
    This will be the main function.
    Provide information as to lives left and art graphics view.
    User will guess the letters until completed,
    or until life has been depleted.
    """
    word = random_word()
    letter_pattern = r'^[a-z]$'
    guessed_letters = set()
    guess_wrong = []
    guess_correct = []
    letter_word = ['_'] * len(word)
    lives = 6
    letter_found = False
    # print(word)   for when testing is needed.

    while lives > 0:
        print(' '.join(letter_word))
        print(f"Ye have {lives} lives left, me hearty! ")
        print(shark.tries_left[6 - lives])
        guess_letter = input("Guess a letter:\n ").lower()
        shark.clear_screen()

        if not re.match(letter_pattern, guess_letter):
            print("Foul value, use one alphabet letter only!")
            continue
        if guess_letter in guessed_letters:
            print("Struck a dud, already used pick a fresh letter!")
            continue

        guessed_letters.add(guess_letter)
        print(guessed_letters)

        if guess_letter in word:
            print(f"Aye, that's correct: {guess_letter}")
            for i, char in enumerate(word):
                if char == guess_letter:
                    letter_word[i] = guess_letter
                    letter_found = True
        else:
            print(f"Nay, matey: {guess_letter}")
            lives -= 1
            letter_found = False

        if "_" not in letter_word:
            print(' '.join(letter_word))
            shark.win_msg(word, name)
            break

    if lives == 0:
        shark.lost_msg(word, guessed_letters, name)


def restart_shark(name, guessed_letters):
    """
    Provides an option to restart the game.
    The user will press Y to start or N to exit.
    """
    while True:
        restart = input(f"Arrr, {name} would ye play again Y/N?\n")
        shark.clear_screen()
        if re.fullmatch(r'^[yYnN]$', restart):
            restart = restart.lower()
            if restart == 'y':
                print(f" Splendid {name}")
                guessed_letters.clear()
                word = random_word()
                guess_word_letter(name, guessed_letters)
            elif restart == 'n':
                shark.exit_msg(name)
                print(f"Arr! Should ye want to paddle again?\n"
                      "Press run program.\n")
                exit()
        else:
            print("Foul value, Y or N only!")


def main():
    """
    To call all other functions in the game
    """
    shark.welcome_msg()
    name = username()
    gamerules(name)
    guessed_letters = []
    guess_word_letter(name, guessed_letters)
    restart_shark(name, guessed_letters)


main()
