"""
Malcolm Wanless
A01365553
"""
import random


def make_board(rows, columns):
	"""
	A function that takes in two integers(rows, columns), and returns a dictionary that represents a gameboard of
	that size (rows x columns), with a descriptor for each room.

	:param rows: a positive integer representing the number of rows on the gameboard
	:param columns: a positive integer representing the number of columns on the gameboard
	:precondition: rows is an integer greater than zero
	:precondition: columns is an integer greater than zero
	:postcondition: the returned dictionary has tuple keys that describe the coordinates of each room, and a string
	value that represents a description of that room
	:return: a dictionary that represents a gameboard of tuple keys and string room descriptions

	>>> make_board(1, 1)
	{(0, 0): "You're in room (0, 0); It is empty."}
	>>> make_board(2, 2)
	{(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.", (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
	>>> make_board(1, 4)
	{(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.", (0, 2): "You're in room (0, 2); It is empty.", (0, 3): "You're in room (0, 3); It is empty."}
	"""
	board_dictionary = {}

	for row in range(rows):
		for column in range(columns):
			board_dictionary[(row, column)] = f'You\'re in room ({row}, {column}); It is empty.'

	return board_dictionary


def make_character():
	"""
	Generate a dictionary that represents a character and their stats.

	A function that takes in no arguments, but returns a character dictionary with starting locations and a health
	value.

	:precondition: none
	:postcondition: a dictionary that represents a character, with character's starting locations and a health value
	:return: a dictionary that contains two key:value paris that represent coordinates and one key:value pair that
	represents health.

	>>> make_character()
	{'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
	"""
	return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


def describe_current_location(board, character):
	"""
	Describe the current location that the character is in.

	A function that takes in the current gameboard and the character object and returns a description of the current
	location, using the coordinates of the character and the description of the current location from the board object.

	:param board: a dictionary containing the current gameboard object
	:param character: a dictionary containing the current character object
	:precondition: board is a dictionary with location data, in tuple keys, with string descriptions
	:precondition: character is a dictionary with location data, and a health key:value pair
	:postcondition: the printed string provides the current location of the character object on the board

	>>> board_1 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty."}
	>>> character_1 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
	>>> describe_current_location(board_1, character_1)
	You're in room (0, 0); It is empty.
	>>> board_2 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is full."}
	>>> character_2 = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
	>>> describe_current_location(board_2, character_2)
	You're in room (0, 1); It is full.
	"""
	print(board[(character["X-coordinate"], character["Y-coordinate"])])


def get_user_choice():
	"""
	Receive user input and validate the selected direction so that it can work with the game board.

	A function that receives no input, but asks the user to input a direction. If the direction is valid, it returns
	the correct integer value. It will keep asking the user for input as long as the inputted value is not 1 to 4,
	inclusive. The direction is valid only if it is one of the four cardinal directions, represented by integer keys,
	and displayed to the user as a string.

	:precondition: none
	:postcondition: the returned integer value is between 1 and 4, inclusive.
	:return: an integer value indicating one of the listed cardinal directions
	"""
	user_directions = {1: "north", 2: "east", 3: "south", 4: "west"}
	valid_user_input = False
	user_direction_input = 0

	while not valid_user_input:
		user_direction_input = int(input("Please input a direction of either 1. North, 2. East, 3. South, "
		                                 "4. West: "))
		if user_direction_input in user_directions:
			valid_user_input = True
		else:
			print("The direction provided doesn't exist in our system; Please try again.")

	return user_direction_input


def validate_move(board, character, direction):
	"""
	Determine whether a direction will extend past the edges of the game board and prevent invalid movement by the
	character if so.

	A function that takes in three arguments: the game board, the character, and a direction. The function will
	determine the current character's position on the board, and whether the passed in direction is a valid move for
	that character to make. If the move is valid, return True. If not, return False.

	:param board: a dictionary containing the current gameboard object
	:param character: a dictionary containing the current character object
	:param direction: an integer, between 1 and 4, inclusive, that represents the movement direction
	:precondition: board is a dictionary with location data, in tuple keys, with string descriptions
	:precondition: character is a dictionary with location data, and a health key:value pair
	:precondition: direction is an integer between 1 and 4
	:postcondition: the returned boolean indicates the validity of the movement on the board
	:return: a boolean value representing the validity of the movement direction

	>>> board_1 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
	... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
	>>> character_1 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
	>>> direction_1 = 2
	>>> validate_move(board_1, character_1, direction_1)
	True
	>>> board_2 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
	... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
	>>> character_2 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
	>>> direction_2 = 4
	>>> validate_move(board_2, character_2, direction_2)
	False
	>>> board_3 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
	... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
	>>> character_3 = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
	>>> direction_3 = 3
	>>> validate_move(board_3, character_3, direction_3)
	False
	"""
	if direction == 1:
		if (character["X-coordinate"], character["Y-coordinate"] - 1) not in board:
			return False
	elif direction == 2:
		if (character["X-coordinate"] + 1, character["Y-coordinate"]) not in board:
			return False
	elif direction == 3:
		if (character["X-coordinate"], character["Y-coordinate"] + 1) not in board:
			return False
	elif direction == 4:
		if (character["X-coordinate"] - 1, character["Y-coordinate"]) not in board:
			return False

	return True


def move_character(character, direction):
	"""
	Move the character to a new location on the board.

	A function that takes in a character dictionary and a direction value. The character's X, or Y coordinate values
	are modified by +1 or -1, depending on which direciton value is passed into the function.

	:param character: a dictionary containing the current character object
	:param direction: an integer, between 1 and 4, inclusive, that represents the movement direction
	:precondition: character is a dictionary with location data, and a health key:value pair
	:precondition: direction is an integer between 1 and 4
	:postcondition: the character object has a modified X, or Y coordinate value that indicates their new position on
	the board

	>>> character_1 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
	>>> direction_1 = 2
	>>> move_character(character_1, direction_1)
	>>> print(character_1)
	{'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
	>>> character_2 = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 5}
	>>> direction_2 = 3
	>>> move_character(character_2, direction_2)
	>>> print(character_2)
	{'X-coordinate': 2, 'Y-coordinate': 4, 'Current HP': 5}
	>>> character_3 = {'X-coordinate': 1, 'Y-coordinate': 3, 'Current HP': 5}
	>>> direction_3 = 1
	>>> move_character(character_3, direction_3)
	>>> print(character_3)
	{'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
	"""
	if direction == 1:
		character["Y-coordinate"] -= 1
	elif direction == 2:
		character["X-coordinate"] += 1
	if direction == 3:
		character["Y-coordinate"] += 1
	elif direction == 4:
		character["X-coordinate"] -= 1


def check_if_goal_attained(character):
	"""
	Check to see if the character has reached the goal, or the designated spot on the board.

	A function that takes in a character object, and checks the goal tuple value of the map goal coordinates against
	the current value of the character's X, and Y coordinate values. If so, return a True boolean value. If not,
	return False.

	:param character: a dictionary containing the current character object
	:precondition: character is a dictionary with location data, and a health key:value pair
	:postcondition: the return value is a boolean that represents whether the character has reached a specific spot on
	the board
	:return: a boolean value representing whether the character has reached the end goal

	>>> character_1 = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
	>>> check_if_goal_attained(character_1)
	False
	>>> character_2 = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
	>>> check_if_goal_attained(character_2)
	True
	"""
	return(character["X-coordinate"], character["Y-coordinate"]) == (2, 2)


def check_for_foes():
	"""
	Check to see if there is a foe on the board at the current location.

	A function that takes in no arguments, but returns a boolean. This represents
	a 25% chance to encounter a foe on the board, at this location.

	:precondition: none
	:postcondition: the returned boolean value represents a 25% chance of receiving any
	one of the four integer values
	:return: a boolean value
	"""
	return random.randint(1, 4) == 1


def guessing_game(character):
	"""
	Play a guessing game and reduce the character HP if the user does not guess the integer value.

	A function that takes in a character object and modifies the HP value if a guessing game is failed. The function
	doesn't return anything, but asks the user for an integer value for input. If the user guesses incorrectly,
	the character loses 1hp. If the user guesses correctly, the character doesn't lose any hp.

	:param character: a dictionary containing the current character object
	:precondition: character is a dictionary with location data, and a health key:value pair
	:postcondition: the character has either reduced HP or the same HP, depending on the result of the guessing game
	"""
	user_input = int(input("I'm attacking you! Guess a number between 1 and 5, inclusive: "))

	enemy_number = random.randint(1, 5)

	if user_input == enemy_number:
		print("Correct! Please continue on.")
	else:
		print("Incorrect! You take one damage! Please continue.")

		character["Current HP"] -= 1


def game():
	"""
	Drive the game
	"""
	rows = 3
	columns = 3
	board = make_board(rows, columns)
	character = make_character()
	achieved_goal = False
	while not achieved_goal and character["Current HP"] > 0:
		describe_current_location(board, character)
		direction = get_user_choice()
		valid_move = validate_move(board, character, direction)
		if valid_move:
			move_character(character, direction)
			describe_current_location(board, character)
			there_is_a_challenger = check_for_foes()
			if there_is_a_challenger:
				guessing_game(character)
			achieved_goal = check_if_goal_attained(character)
		else:
			print("Nice try, but that direction isn't valid! Please try again.")

	if character["Current HP"] > 0:
		print("Congrats on getting to the end! You win!")
	else:
		print("Sorry you didn't survive the game! Better luck next time.")


def main():
	"""
	Drive the program
	"""
	game()


if __name__ == "__main__":
	main()
