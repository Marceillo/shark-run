# Shark-Run 

Welcome to Shark-Run live program [Shark-Run](https://shark-run-e1a617839e7e.herokuapp.com/).

The game is a word-guessing game similar to the old hangman game.
Only in this game, do you have a kayaker and a shark chasing the kayaker.
The reality is we should learn to live in the same world with each other and learn from each other.
The dictionary words are based on the shark and kayak words.

![Welcome](gallery/welcome-message.png)


# Contents
* [**Shark.Run**](#shark-run)
* [**User Experience**](#user-experience)
    * [User Stories](#user-stories)
    * [Creation Process](#creation-process)
    * [Design Choices](#design-choices)
    * [Colour used from colorama ](#colorama)
* [**How to play**](#how-to-play)
* [**Features**](#features)
   * [Existing Features](#existing-Features)                        
   * [**Inspiration**](<#inspiration>)
   * [**Future Features**](<#future-features>)
* [**Data Model**](<#data-model>)   
* [**Technologies Used**](<#technologies-used>)
* [**Python Packages**](<#python-packages>)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Credits**](#credits)
* [**Acknowledgements**](#acknowledgements)
  
# User Experience

## User Stories
### Primary Goal 
### Visitor Goal

## Creation Process
### Planning
### Flow chart 

- The flow chart was the start of this project to make a rough idea of how the game is going to work.
- It helped organize what section to do first and what was next to do
- It created a structure of which function should start and where to end.

![Flow chart](gallery/flow_chart.png)
  
## Design Choices

- The app is built in a display window of 80 characters per line and a max of 24 
  lines.
- dependencies  requirements.txt
- I wanted the game to flow from one function to the next in the  Python language.
- I created a helper file called shark as this helped to keep the code easy to read in the main code file.
- The helper file also keeps all the art and added functions, to a minimum in the main code.
- This makes for easier implementation and error handling.
- The language used is an old sailer nautical language as it fits with them and is different.
- It might be a little strange language for some to understand at first but it makes sense as you go along with it.
- after the welcome message the player has an opportunity to insert a player name or username for a better word.
- Certain message have asciiart as this personilized the experience with often the username displayed and information in others.
- The asciiart also plays also a role in displaying an color changin image indicating to the user that they are reaching critical life 
  levels.
- Implemented error message should they have used the incorrect value.   
  
## Colour used from colorama  

- I used some of the colors provided by Colorama (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
- For this game, I chose CYAN as it is the closer color to the ocean for the start of the game.
- Other colors were YELLOW and RED to signify to the user the shark is getting closer with each incorrect answer.
- GREEN was used for the instructions and when you win the game. 


## How to play

- You have to guess the letter of the hidden word and the words are related to shark and kayak.
- When you guess incorrectly the shark gets closer to your kayak.
- You have six lives, So you have six times to guess the letters of the word.
- If you do guess correct a life will not be deducted.
- If you use other letters and characters it will give you a error but a life won't be deducted.

![Instructions](gallery/instructions.png)

[Back to top](#contents)

## Features

### Existing Features

- Plain 

#### Inspiration

- I wanted somthing differant that matches my interests and hobbys.
- One of my hobbys is kayaking this is where I got the insperation to make this game.
  
#### Future Features

 - Function 
 
## Data Model
   
## Technologies Used

- [Gitpod](https://www.gitpod.io/#get-started) - used to deploy the website.
- [Github](https://github.com/) - used to host and edit the website.
- [Python](https://www.python.org/) 
- [perplexity](https://www.perplexity.ai/) - This was used for the dictionery and the Nautical language used in the game.
- [PEP8ci](https://pep8ci.herokuapp.com/#) - This was used to validate.
- [Heruku](https://id.heroku.com/login) - Used to deploy the game.
- [Asciiart](https://www.asciiart.eu) - Used for the display art.

## Python Packages

- [Colorama](https://pypi.org/project/colorama/)
- [Time](https://docs.python.org/3/library/time.html)
- [OS](https://docs.python.org/3/library/os.html)
- [Random](https://docs.python.org/3/library/random.html)

[Back to top](#contents)
  
## Testing 

### Manual Testing

### Validator Testing 

- [Pep8ci](https://pep8ci.herokuapp.com/#)
     

- ![Pep8ci](assets/images/desktop-lighthouse.png)
            
- cleared errors Result

- ![Pep8ci](assets/images/mobile-lighthouse.png)

   

### Fixed Bugs

- game problems 

### Unfixed Bugs
 
- Unfixed bugs 

[Back to top](#contents)

## Deployment

Deployed the site on GitHub using the following procedure:
-Heruku
1. By

The instruction link below on how to fork a project:

[Fork the project](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

The instruction link below on how to clone a project:

[Clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 

## Credits 

- [W3schools](https://www.w3schools.com/)
- [Stackoverflow](https://stackoverflow.com/)
- [Youtube](youtube.com)
- [W3docs](https://www.w3docs.com/)

### Content

### Media



## Acknowledgements

- I would like to thank my fellow student Sebastian Kefer for providing good troubleshooting ideas when I was stuck on bugs or problems it is nice to have support in these times.
- Thank you to my mentor who has helped guide me in this project.

[Back to top](#contents)   