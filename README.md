
# Ultimate Battleship

Ultimate Battleship is a Python terminal game, which runs on Heroku.

The goal of the game is for the users to find all of the computer's battleships before the computer finds theirs.
Each battleship occupies one square on the board.

[Here is the live version of my project](https://project-portfolio-three.herokuapp.com/)

![Responsive Mockup](/readme-docs/responsive.jpg)
## How to play

Ultimate Battleships is based on the popular board game. 

In this version, the player enters their name, chooses the size of the board (5x5 - 8x8) and the number of ships (4-6).

Then two board are generated and randomly populated with ships.

The player can see where their ships are, indicated by an `@` sign, but cannot see where the computer ships are.

Guesses are marked on the board with an `X`. Hits are marked with a `*`.

The player and the computer then take it in turns to make guesses and try and sink each other's battleships.

The winner is whoever sinks all of their opponent's battleships first.
## Features

### Existing Features

- User select name, board size and number of ships
    - All inputs are validated and checked for errors
    - Name cannot be whitespaces
    - Board size and number of ships must be a number between the indicated values

![Game Start Checks](/readme-docs/other-checks.jpg)

- Random board generation
    - Ships are randomly placed on both the player and computer boards
    - Player cannot see where computer's ships are

![Game Setup](/readme-docs/game-setup.jpg)

- Play against the computer
- Accept user input
- Mantain score

![Running Game](/readme-docs/running-game.jpg)

- Input validation and error-checking
    - User cannot enter coordinates outside of the board size
    - User must enter a number
    - User cannot guess same coordinates twice

![Guesses checks](/readme-docs/guess-check.jpg)

- Data maintained in class instances

### Future Features

- Allow player to position ships themselves
- Have ships larger than 1x1


## Data Model

I was provided the Board class model. The game creates two instances of the Board class to hold the player's and computer's boards.

The Board class stores board size, number of ships, position of ships, guesses against that board,
and details such as board type (player or computer) and player's name.

The class also has methods to help the game, such as a `print` method to print out the current board
an `add_ships` method to add ships onto the board and an `add_guess` method to add guesses and return results(hit or miss).

## Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no issues
- Given invalid inputs: strings where number are expected, out of bound inputs, same input twice, wrong board sizes and wrong number of ships
- Tested in my local terminal and on Heroku terminal

### Bugs

#### Solved Bugs

- My `populate_board` function initially was occasionally placing multiple ships on the same square on the board. I added code to check if the new coordinates are already present in the `board.ships` list and the problem was easily solved.
- My `make_guess` function initially was allowing the computer to guess the same coordinates more than once, again solved easily by adding code to check that new computer guess is not already present in `board.guesses` list.

### Remaining Bugs

- No remaining Bugs

### Validator Testing

- PEP8
    - No errors were returned from pep8ci.herokuapp.com
## Deployment

This project was deployed on Heroku.

- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to `Python` and `NodeJS` in that order
    - Link the Heroku app to the repository
    - Click on **Deploy**


## Credits

- Code Institute provided me with the basis of this project, including the `Board` class, the `random_point()` helper function and the `new_game()` function