from colorama import Fore
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

trys_left = [
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
""", r"""
         .-'-.
       /`     |__
     /`  _.--`-,-`
     '-|`   a '<-.   []
       \     _\__) \=`
        C_  `    ,_/
          | ;----'
          """)

def correct_name(user_name): return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}, ye scallywags!                                                   
Lend us a hand to keep the briny deep safe, if ye please.                     
Guess the words right, so the shark learns that the kayakers be no vittles for
the likes of 'im!                                                             
Should ye want to see the rules, press Y or N.                                
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def incorrect_name(user_name): return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}, ye scallywag!                                                 
Yer handle should be naught but letters, from A to Z, both upper and lower,
and be no shorter than a single letter and no longer than fifteen,         
with no other scurvy characters like numbers or symbols or the like!"      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def exit_msg(user_name): return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{user_name}! Arr, ye scallywags, it pains me heart to see ye shove off.
But take heart, for I know ye'll be back to join us once more, aye?    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def instructions():
  print(Fore.CYAN + r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                        Instructions                           ~
~The game is a word-guessing game similar to the Hangman game.  ~
~All the words are related to sharks and kayak them.            ~
~You will need to guess each letter of the word.                ~
~When you get it wrong the shark will get closer to the kayaker.~
~You have six tries to guess the word.                          ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")


print(Fore.RESET)

