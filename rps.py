"""
rps.py

Redistributed and modified with permission from the
EECS Department at The University of Michigan, Ann Arbor

Name: Adrion Mercer

CS 104: Project 2
FALL 2026

Description: A two-player Rock, Paper, Scissors game that plays three rounds and determines the winner.
"""

# ***********************************************************************
# Constants. Global constants are fine. Global variables are not.
# Use these names in your code instead of typing the raw values.
# ***********************************************************************
COURSE_NAME = "CS 104"
MAX_ROUNDS = 3

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
DEFAULT_MOVE = ROCK

PLAYER_1 = 1
PLAYER_2 = 2
DEFAULT_NAME_1 = "Rocky"
DEFAULT_NAME_2 = "Creed"

DRAW = 0

ERROR_NAME = 1
ERROR_MOVE = 2

PLAY_RPS = 1
PLAY_RPSLS = 2
QUIT_CHOICE = 3

# ***********************************************************************
# The following four functions have already been implemented for you.
# You should use them when writing the other functions, but do not edit
# their implementations. You will find them at the bottom of this file.
# ***********************************************************************

# print_initial_header()
#
# Purpose:     Prints a pretty header to introduce the user to the game.
#
#
# print_menu()
#
# Purpose:     Prints the menu.
#                  "1) Play rock, paper, scissors"
#                  "2) Play rock, paper, scissors, lizard, spock"
#                  "3) Quit"
#              It does NOT print the "Choice --> " prompt. Your
#              get_menu_choice() does that with input().
#
#
# print_error_message(error_number)
#
# Purpose:     If error_number is ERROR_NAME, prints an error message
#              indicating an illegal name was entered.
#              If error_number is ERROR_MOVE, prints an error message
#              indicating an illegal move was entered.
# Parameters:  error_number - what error to be printed
# Constraint:  error_number must be ERROR_NAME or ERROR_MOVE
#
#
# print_closer()
#
# Purpose:     Prints out the final greeting for the program.

# ***********************************************************************
# You must implement all of the following functions. Add your
# implementations below rps() as indicated. The specs below tell you what
# each function must do. Write your own def line and give every function
# a short docstring (one or two lines is fine).
# ***********************************************************************

# get_name(player_number)
#
# Purpose:     Prompts the user to enter their name. Names entered may
#              have spaces within them.
#                  Example: "Kermit the frog"
#
#              If an empty name is given, this is invalid input, so call
#              print_error_message with ERROR_NAME and return a default
#              name.
#              For player 1, the default name is: Rocky
#              For player 2, the default name is: Creed
# Parameters:  player_number - the player whose name will be assigned
# Constraint:  player_number is either PLAYER_1 or PLAYER_2
# Returns:     the name as a string
# Prompt:      Player 1, enter your name:   (Player 2 for the second)
#
#
# get_menu_choice()
#
# Purpose:     Prints the menu, and reads the input from the user.
#              Checks to make sure the input is within range for the
#              menu. If it is not, prints "Invalid menu choice".
#              Continues to print the menu and read in input until a
#              valid choice is entered, then returns the user's choice
#              of menu options.
#              A user could type anything at this prompt, not only
#              numbers. Anything other than 1, 2 or 3 is invalid.
# Returns:     the choice as an int (1, 2 or 3)
# Prompt:      Choice -->
# Hint:        input() gives you a string. Check the string first. Cast
#              it to an int once you know it is valid.
#
#
# is_move_good(move)
#
# Purpose:     Checks for valid move. Returns True if and only if move
#              represents a valid move: one of "R", "r", "P", "p", "S",
#              "s". Returns False otherwise.
# Parameters:  move - input provided by user. It is a string but it can
#              be any length, even empty.
# Returns:     True or False
#
#
# get_move(player_name)
#
# Purpose:     Prompts the player for their move and returns it. If an
#              illegal move is entered, call print_error_message with
#              ERROR_MOVE and return rock (DEFAULT_MOVE) as a default.
#              You can assume the user presses Enter after typing.
# Parameters:  player_name - the name of the player being prompted for
#              their move
# Returns:     the move as a string, exactly as typed unless it was
#              invalid
# Prompt:      [player_name], enter your move:
#
#
# is_round_winner(move, opponent_move)
#
# Purpose:     Returns True if and only if the player who made move won
#              according to the rules of Rock, Paper, Scissors. Returns
#              False otherwise. A tie is not a win.
# Parameters:  move - the move of the player being checked for a win
#              opponent_move - the move of the opponent
# Constraint:  move and opponent_move must both be valid moves
# Returns:     True or False
#
#
# announce_round_winner(winner_name)
#
# Purpose:     If winner_name is empty, prints a message indicating the
#              round is a draw. Otherwise, prints a congratulatory
#              message to the winner.
# Parameters:  winner_name - the name of the player who won the round
#              (an empty string for a draw)
# Constraint:  winner_name must be the correct winner
# Prompt:      This round is a draw!
#              ------------- OR -------------
#              [winner_name] wins the round!
#
#
# do_round(p1_name, p2_name)
#
# Purpose:     Simulates a complete round of rock, paper, scissors,
#              which consists of three steps:
#                1. Get player 1's move
#                2. Get player 2's move
#                3. Return DRAW if the round was a draw; PLAYER_1 if
#                   player 1 won; PLAYER_2 if player 2 won.
#              It does not announce anything. do_game does that.
# Parameters:  p1_name and p2_name - the names of the respective players
# Returns:     DRAW (0), PLAYER_1 (1) or PLAYER_2 (2)
#
#
# announce_winner(winner_name)
#
# Purpose:     If winner_name is empty, prints that there was no winner.
#              Otherwise, prints a congratulatory message to the winner.
# Parameters:  winner_name - the name of the player who won the game
# Prompt:      No winner!
#              ------------- OR -------------
#              Congratulations [winner_name]!
#              You won CS 104 Rock, Paper, Scissors!
#              (use COURSE_NAME for "CS 104")
#
#
# do_game(p1_name, p2_name, game_type)
#
# Base Project:
# Purpose:     If game_type is PLAY_RPSLS, prints "Under Construction"
#              to indicate that rock, paper, scissors, lizard, spock has
#              not been implemented. Returns an empty string.
#              Otherwise, plays exactly MAX_ROUNDS rounds of
#              rock-paper-scissors while keeping track of the number of
#              round wins for each player. When a round results in a
#              draw, neither player is the winner, so neither player is
#              awarded a point. All rounds are played, even if one
#              player has already won the game.
#              After each round is played, the round winner (or draw) is
#              announced. Returns the name of the winner or an empty
#              string if the game ended in a draw.
# Parameters:  p1_name and p2_name - the names of the respective players
#              game_type - PLAY_RPS for regular rock, paper, scissors
#              or PLAY_RPSLS for rock, paper, scissors, lizard, spock
# Returns:     the winner's name as a string, or "" for no winner
# Prompt:      Under Construction


def rps():
    """Runs the whole Rock, Paper, Scissors program.  """
    print_initial_header()

    p1_name = get_name(PLAYER_1)
    p2_name = get_name(PLAYER_2)

    while True:
        choice = get_menu_choice()

        if choice == QUIT_CHOICE:
            break

        winner_name = do_game(p1_name, p2_name, choice)
        announce_winner(winner_name)

    print_closer()


# ***********************************************************************
# Add all function implementations below this line.
# We have started is_move_good() for you.
# ***********************************************************************

def is_move_good(move):
    """Returns True when move is rock, paper, or scissors."""
    move = move.lower() 

    if move == ROCK or move == PAPER or move == SCISSORS:
        return True
    else:
        return False

def is_round_winner(move, opponent_move):
    """Returns True if the first move beats the opponent's move."""
    move = move.lower()
    opponent_move = opponent_move.lower()

    if move == ROCK and opponent_move == SCISSORS:
        return True
    elif move == PAPER and opponent_move == ROCK:
        return True
    elif move == SCISSORS and opponent_move == PAPER:
        return True
    else:
        return False
def get_name(player_number):
    """ Gets the player's name or returns a default name if empty."""
    name = input(f"player {player_number}, enter your name: ")

    if name =="":
        print_error_message(ERROR_NAME)

        if player_number == PLAYER_1:
            return DEFAULT_NAME_2
    return name
def get_menu_choice():
    """Displays the menu and returns a valid mwnu choice."""
    while True:
        print_menu()
        choice = input("choice --> ")

        if choice == "1" or choice =="2" or choice == "3":
            return int(choice)
        else:
            print("invalid menu choice")
def get_move(player_name):
    """Gets a player's move and uses rock if the move is invalid."""
    move = input(f"{player_name}, enter your move: ")

    if is_move_good(move):
        return move
    else:
        print_erroe_message(ERROR_MOVE)
        return DEFAULT_MOVE
def announce_round_winner(winner_name):
    "prints the winner of the round or announces a draw."""
    if winner_name == "":
        print("this round is a drwa!")
    else:
        print(f"{winner_name} wins the round!")

def do_round(p1_name, p2_nae):
    """palys one round and returns the result."""
    p1_move = get_move(P1_name)
    p2_move = get_move(P2_name)

    if p1_move.lower() == p2_move.lower():
        return DRAW
    elif is_round_winner(P1_move, P2_move):
        return PLAYER_1
    else:
        return PLAYER_2


   def announce_winner(winner_name):
    """Prints the game winner or announces that there was no winner."""
    if winner_name == "":
        print("No winner!")
    else:
        print(f"Congratulations {winner_name}!")
        print(f"You won {COURSE_NAME} Rock, Paper, Scissors!") 
  def do_game(p1_name, p2_name, game_type):
    """Plays three rounds and returns the name of the game winner."""

    if game_type == PLAY_RPSLS:
        print("Under Construction")
        return ""

    p1_wins = 0
    p2_wins = 0

    for round_number in range(MAX_ROUNDS):
        result = do_round(p1_name, p2_name)

        if result == PLAYER_1:
            p1_wins += 1
            announce_round_winner(p1_name)

        elif result == PLAYER_2:
            p2_wins += 1
            announce_round_winner(p2_name)

        else:
            announce_round_winner("")

    if p1_wins > p2_wins:
        return p1_name
    elif p2_wins > p1_wins:
        return p2_name
    else:
        return ""
        
# ***********************************************************************
# DO NOT modify the four functions below.
# ***********************************************************************
def print_initial_header():
    """Prints a pretty header to introduce the user to the game."""
    print("----------------------------------------")
    print("                CS 104")
    print("          Rock, Paper, Scissors")
    print("----------------------------------------")


def print_menu():
    """Prints the menu options (not the prompt)."""
    print()
    print("Menu Options")
    print("------------")
    print("1) Play rock, paper, scissors")
    print("2) Play rock, paper, scissors, lizard, spock")
    print("3) Quit")
    print()


def print_error_message(error_number):
    """Prints the error for ERROR_NAME or ERROR_MOVE."""
    if error_number == ERROR_NAME:
        print()
        print("ERROR: Illegal name given, using default")
        print()
    elif error_number == ERROR_MOVE:
        print()
        print("ERROR: Illegal move given, using default")
    else:
        print("This should never print!")


def print_closer():
    """Prints out the final greeting for the program."""
    print()
    print("----------------------------------------")
    print("           Thanks for playing")
    print("          Rock, Paper, Scissors!")
    print("----------------------------------------")
