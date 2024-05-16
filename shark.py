from colorama import Fore
import os
import time

words = [
    'kayak',
    'shark',
    'paddle',
    'glide',
    'fins',
    'teeth',
    'thrash',
    'spray',
    'rudder',
    'chomp',
    'stern',
    'bow',
    'fluke',
    'reef',
    'surge',
    'fathom',
    'buoy',
    'gills',
    'leash',
    'tails',
]

tries_left = [
   Fore.CYAN + r'''
        \
          \   O,
\___________\/ )_________/
~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/"*._         _
                \                             .-*'`    `*-.._.-'/
                                           < * ))     ,       (
                                             `*-._`._(__.--*"`.\

    ''', Fore.CYAN + r'''
         \
           \   O,
 \___________\/ )_________/
~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/"*._         _
                 \                      .-*'`    `*-.._.-'/
                                     < * ))     ,       (
                                       `*-._`._(__.--*"`.\
    ''', Fore.YELLOW + r'''
        \
          \   O,
\___________\/ )_________/
~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~/"*._         _
                \                 .-*'`    `*-.._.-'/
                                < * ))     ,       (
                                   `*-._`._(__.--*"`.\
    ''', Fore.YELLOW + r'''
        \
          \   O,
\___________\/ )_________/
~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~/"*._         _
                \          .-*'`    `*-.._.-'/
                         < * ))     ,       (
                           `*-._`._(__.--*"`.\
    ''', Fore.RED + r'''
        \
          \   O,
\___________\/ )_________/
~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~/"*._         _
                 \       .-*'`    `*-.._.-'/
                       < * ))     ,       (
                          `*-._`._(__.--*"`.\
    ''', Fore.RED + r'''
        \
          \   O,
\___________\/ )_________/
~~~~~~~~~~~~~~ \~~~~~~~/"*._         _
                 \.-*'`    `*-.._.-'/
                < * ))     ,       (
                  `*-._`._(__.--*"`.\
    ''']


# Welcome display message for the game.
def welcome_msg():
    print(Fore.CYAN + r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~    _    _                                     _             _ ~
~   / \  | |__   ___  _   _     _ __ ___   __ _| |_ ___ _   _| |~
~  / _ \ | '_ \ / _ \| | | |   | '_ ` _ \ / _` | __/ _ \ | | | |~
~ / ___ \| | | | (_) | |_| |_  | | | | | | (_| | ||  __/ |_| |_|~
~/_/   \_\_| |_|\___/ \__, ( ) |_| |_| |_|\__,_|\__\___|\__, (_)~
~__        __   _     |___/|/                _          |___/   ~
~\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___            ~
~ \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \           ~
~  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |          ~
~ __\_/\_/ \___|_|\___\___/|_| |_|_|_|\___|  \__\___/           ~
~/ ___|| |__   __ _ _ __| | __ |  _ \ _   _ _ __                ~
~\___ \| '_ \ / _` | '__| |/ / | |_) | | | | '_ \               ~
~ ___) | | | | (_| | |  |   <  |  _ <| |_| | | | |              ~
~|____/|_| |_|\__,_|_|  |_|\_\ |_| \_\\__,_|_| |_|              ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    time.sleep(6)
    clear_screen()


def correct_name(user_name): return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}, ye scallywags!
end us a hand to keep the briny deep safe, if ye please.
Guess the words right, so the shark learns that the kayakers be no vittles for
the likes of 'im!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def incorrect_name(user_name): return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}, ye scallywag!
Yer handle should be naught but letters, from A to Z, both upper and lower,
and be no shorter than a single letter and no longer than fifteen,
with no other scurvy characters like numbers or symbols or the like!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def exit_msg(user_name):
    print(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}! Arr, ye scallywags, it pains me heart to see ye shove off.
But take heart, for I know ye'll be back to join us once more, aye?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")


def instructions():
    print(Fore.GREEN + r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                        Instructions                           ~
~The game is a word-guessing game similar to the Hangman game.  ~
~All the words are related to sharks and kayak them.            ~
~You will need to guess each letter of the word.                ~
~When you get it wrong the shark will get closer to the kayaker.~
~You have six tries to guess the word.                          ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")


def win_msg(word, user_name):
    print(Fore.GREEN + rf"""
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)

             .-'-.
           /`     |__
         /`  _.--`-,-`
         '-|`   a '<-.   []
           \     _\__) \=`
            C_  `    ,_/   Aye, correctly guessed word is {word}.
              | ;----'

               Splendid {user_name} catch, me hearty! Bravo, well won!
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)
""")


def lost_msg(word, guessed_letters, user_name):
    print(Fore.RED + rf"""
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)

           .-'-.
         /`     |__
       /`  _.--`-,-`
       '-|`   a '<-.   []
         \     _\__) \=`
          C_  `    ,_/
            | ;----'
  Arr! the correct word is {word}.
  Your incorrect guessed letters is\n {guessed_letters}.

  Ye be out of luck, {user_name}. Better luck next time!
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)
""")


print(Fore.RESET)


# Used code from www.geeksforgeeks.org and https://stackoverflow.com/
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
