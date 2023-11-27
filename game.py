"""
Malcolm Wanless
A01365553
"""
import random


def make_board():
	board_dictionary = {(row, column): f'You\'re in room ({row}, {column}); It is empty.' for row in range(0, 5) for
	                    column in range(0, 5)}
	board_dictionary.update({(row, column): f'You\'re in room ({row}, {column}); It is empty.' for row in range(0,
	                                                                                                            5) for
	                         column in range(6, 11)})
	board_dictionary.update({(row, column): f'You\'re in room ({row}, {column}); It is empty.' for row in range(0,
	                                                                                                            5) for
	                         column in range(12, 17)})
	board_dictionary.update({(row, column): f'You\'re in room ({row}, {column}); It is empty.' for row in range(1,
	                                                                                                            4) for
	                         column in range(18, 21)})
	board_dictionary.update({(2, 5): f'You\'re in room ({2}, {5}): There is a door here.'})
	board_dictionary.update({(2, 11): f'You\'re in room ({2}, {11}): There is a door here.'})
	board_dictionary.update({(2, 17): f'You\'re in room ({2}, {17}): There is a door here.'})

	# for row in range(5):
	# 	for col in range(21):
	# 		if (row, col) in board_dictionary.keys():
	# 			print(board_dictionary[(row, col)])

	return board_dictionary


def make_character():
	print("Character made")
	return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


def describe_current_location(board, character):
	print(board[(character["Y-coordinate"], character["X-coordinate"])])


def get_user_choice():
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
	if direction == 1:
		if (character["Y-coordinate"] - 1, character["X-coordinate"]) not in board:
			return False
	elif direction == 2:
		if (character["Y-coordinate"], character["X-coordinate"] + 1) not in board:
			return False
	elif direction == 3:
		if (character["Y-coordinate"] + 1, character["X-coordinate"]) not in board:
			return False
	elif direction == 4:
		if (character["Y-coordinate"], character["X-coordinate"] - 1) not in board:
			return False

	return True


def move_character(character, direction):
	if direction == 1:
		character["Y-coordinate"] -= 1
	elif direction == 2:
		character["X-coordinate"] += 1
	if direction == 3:
		character["Y-coordinate"] += 1
	elif direction == 4:
		character["X-coordinate"] -= 1


# def check_if_goal_attained(character):
#
# 	return(character["X-coordinate"], character["Y-coordinate"]) == (2, 2)
#
#
# def check_for_foes():
#
# 	return random.randint(1, 4) == 1
#
#
# def guessing_game(character):
#
# 	user_input = int(input("I'm attacking you! Guess a number between 1 and 5, inclusive: "))
#
# 	enemy_number = random.randint(1, 5)
#
# 	if user_input == enemy_number:
# 		print("Correct! Please continue on.")
# 	else:
# 		print("Incorrect! You take one damage! Please continue.")
#
# 		character["Current HP"] -= 1
#

def game():
	"""
	Drive the game
	"""
	rows = 3
	columns = 3
	board = make_board()
	character = make_character()
	achieved_goal = False
	while not achieved_goal and character["Current HP"] > 0:
		describe_current_location(board, character)
		direction = get_user_choice()
		valid_move = validate_move(board, character, direction)
		if valid_move:
			move_character(character, direction)
			describe_current_location(board, character)
		else:
			print("Nice try, but that direction isn't valid! Please try again.")

#       (new version from sample code flow) there_is_a_challenge = check_for_challenges()
# 		there_is_a_challenger = check_for_foes()
# 		if there_is_a_challenger: (challenge)
#           (new version from sample code flow)
#           execute_challenge_protocol(character)
#           if character_has_leveled():
# 	            execute_glow_up_protocol()
#           (remove the below eventually as the above shows new if statement)
# 			guessing_game(character)
#       (add board to achieved_goal, like so: achieved_goal = check_if_goal_attained(board, character))
# 		achieved_goal = check_if_goal_attained(character)

#
# if character["Current HP"] > 0:
# 	print("Congrats on getting to the end! You win!")
# else:
# 	print("Sorry you didn't survive the game! Better luck next time.")
#

def main():
	"""
	Drive the program
	"""
	game()


if __name__ == "__main__":
	main()
