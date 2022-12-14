from random import randint

scores = {'computer': 0, 'player': 0}


class Board:
    """
    Main board class. Sets board size, number of ships,
    player's name and board type(player or computer).
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [['.' for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(' '.join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'
        
        if (x, y) in self.ships:
            self.board[x][y] = '*'
            return 'Hit'    
        else:
            return 'Miss'

    def add_ship(self, x, y, type='computer'):
        if len(self.ships) >= self.num_ships:
            print('Error: you cannot add any more ships!')
        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = '@'


def random_point(size):
    """
    Helper function to return a random integer between 0 and size.
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Checks that the coordinates provided are positive integers,
    that they don't hit outside the board boundaries and that
    they have not been provided already.
    """
    size = board.size - 1
   
    coordinates = (x, y)
    if coordinates in board.guesses:
        print('You cannot guess the same coordinates more than once.')
        return False
    else:
        if (x < 0) or (y < 0) or (x > size) or (y > size):
            print(f'Values must be between 0 and {size}!')
            return False
        else:
            return True


def populate_board(board):
    """
    Populates the board with a randomly placed ship.
    """
    while True:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) in board.ships:
            continue
        else:
            board.add_ship(x, y)
            break

    return board


def make_guess(board):
    """
    For player asks for coordinates, making sure they are numbers
    and for computer generates rondom coordinates. Then uses
    those coordinates with the guess method on both board types.
    Depending on what the guess method returns, it displays the guesses
    and if it was a hit or a miss.
    """
    if board.type == 'computer':
        while True:
            try:
                x = int(input('Guess a row:\n'))
                y = int(input('Guess a column:\n'))
                if valid_coordinates(x, y, board) is True:
                    break
            except ValueError:
                print('You must enter a number!')
            
        if board.guess(x, y) == 'Hit':
            print(f'Player guessed: ({x}, {y})')
            print('Player hits!')
            scores['player'] += 1
        else:
            print(f'Player guessed: ({x}, {y})')
            print('Player missed this time.')
    else:
        x = random_point(board.size)
        y = random_point(board.size)
        if board.guess(x, y) == 'Hit':
            print(f'Computer guessed: ({x}, {y})')
            print('Computer hits!')
            scores['computer'] += 1
        else:
            print(f'Computer guessed: ({x}, {y})')
            print('Computer missed this time.')
    
    return board


def play_game(computer_board, player_board):
    """
    Asks the player for coordinates input and generates computer
    coordinates until someone's score is equal to the number of ships.
    Then it shows a different message depending on the outcome
    of the game(player wins, computer wins, draw).
    """
    name = player_board.name
    p_ships = player_board.num_ships
    c_ships = computer_board.num_ships
    while (scores['player'] < p_ships) and (scores['computer'] < c_ships):
        make_guess(computer_board)
        make_guess(player_board)
        print('-' * 35)
        print('After this round the score are:')
        print(f"{name}: {scores['player']}. Computer: {scores['computer']}")
        print('-' * 35)
        print(f"{name}'s Board:")
        player_board.print()
        print("Computer's Board:")
        computer_board.print()
        print(player_board.guesses)
        print(computer_board.guesses)
    
    if scores['player'] > scores['computer']:
        print('-' * 35)
        print(f'{player_board.name} wins!')
        print('Congratulations!')
        print('-' * 35)
    elif scores['player'] < scores['computer']:
        print('-' * 35)
        print('Computer wins!')
        print('Better luck next time!')
        print('-' * 35)
    else:
        print('-' * 35)
        print('All ships are sanked!')
        print("It's a draw!")
        print('-' * 35)


def new_game():
    """
    Starts new game. Sets board size and number of ships, resets the
    scores and initialises the board.
    """

    size = 5
    num_ships = 4
    scores['computer'] = 0
    scores['player'] = 0
    print('-' * 35)
    print('Welcome to ULTIMATE BATTLESHIPS!!')
    print(f"Board size: {size}. Number of ships: {num_ships}")
    print('Top lef corner is row: 0, col: 0')
    print('-' * 35)
    player_name = input('Please enter your name: \n')
    print('-' * 35)

    computer_board = Board(size, num_ships, 'Computer', type='computer')
    player_board = Board(size, num_ships, player_name, type='player')

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    print(f"{player_name}'s Board:")
    player_board.print()
    print("Computer's Board:")
    computer_board.print()
    print(computer_board.ships)
    play_game(computer_board, player_board)


new_game()
