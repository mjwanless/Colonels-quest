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
	                         column in range(18, 20)})
	board_dictionary.update({(2, 5): f'You\'re in room ({2}, {5}): There is a door here.'})
	board_dictionary.update({(2, 11): f'You\'re in room ({2}, {11}): There is a door here.'})
	board_dictionary.update({(2, 17): f'You\'re in room ({2}, {17}): There is a door here.'})
	board_dictionary.update({(2, 20): f'You\'re in room ({2}, {20}): This is the end of the game.'})

	return board_dictionary


def make_character():
	print("Character made")
	return {
		"X-coordinate": 0,
		"Y-coordinate": 0,
		"Current HP": 25,
		"Max HP": 25,
		"Max Mana": 100,
		"Current Mana": 100,
		"Exp": 0,
		"Current Level": 1}


def make_hen():
	return {"Current HP": 15, "Max HP": 15, "Exp Value": 1}


def make_silkie():
	return {"Current HP": 30, "Max HP": 30, "Exp Value": 3}


def make_rooster():
	return {"Current HP": 50, "Max HP": 50, "Exp Value": 0}


def make_sanders():
	return {"Current HP": 100, "Max HP": 100, "Exp Value": 0}


def holy_blast(character):
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.randint(1, 6)

	return damage_sum


def smite(character):
	character["Current Mana"] -= 15
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.randint(1, 10)

	return damage_sum


def feather_throw():
	damage_sum = 0
	for attack in range(random.randint(1, 4)):
		damage_sum += random.randint(1, 3)

	return damage_sum


def flavour_blast():
	random_num = random.randint(1, 20)

	if random_num <= 4:
		return 4
	elif random_num <= 8:
		return 8
	elif random_num <= 12:
		return 10
	elif random_num <= 16:
		return 12
	elif random_num <= 19:
		return 15
	else:
		return 20


def talons():
	damage_sum = 0
	for attack in range(3):
		damage_sum += random.choice((2, 4, 6))

	return damage_sum


def deep_fry():
	return random.randint(5, 10)


def herbs_and_spices():
	damage_sum = 0
	for attack in range(11):
		damage_sum += random.randint(0, 2)

	return damage_sum


def plumage():
	return random.randint(1, 5)


def scratch():
	return random.choice((1, 2, 3))


def peck():
	return random.choice((1, 2, 4, 0))


def judgement(character):
	character["Current Mana"] -= 30
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.choice((0, 4, 8))

	return damage_sum


def breading():
	heal_sum = 0
	for attack in range(random.randint(1, 3)):
		heal_sum += random.randint(2, 6)

	return heal_sum


def heal(character):
	character["Current Mana"] -= 20
	heal_sum = 0
	for attack in range(character["Current Level"]):
		heal_sum += random.randint(3, 10)

	return heal_sum


def regen_mana(character):
	character["Current Mana"] += 7 + character["Current Level"] * 3


def post_fight_heal(character):
	character["Current Mana"] += 10
	character["Current HP"] += 5


def describe_current_location(board, character):
	for row in range(5):
		for col in range(21):
			if character["Y-coordinate"] == row and character["X-coordinate"] == col:
				print("[*]", end=" ")
			elif (row, col) in board.keys():
				print("[ ]", end=" ")
			else:
				print("   ", end=" ")
		print("\n")

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


def check_if_goal_attained(character):
	return (character["X-coordinate"], character["Y-coordinate"]) == (20, 2)


def check_for_foes():
	return True
	# return random.randint(1, 4) == 1


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
	board = make_board()
	character = make_character()
	achieved_goal = False
	# Put game story function here (just prints out the story)
	describe_current_location(board, character)

	while not achieved_goal and character["Current HP"] > 0:
		direction = get_user_choice()
		valid_move = validate_move(board, character, direction)
		if valid_move:
			move_character(character, direction)
			describe_current_location(board, character)
			if (character["X-coordinate"], character["Y-coordinate"]) == (19, 2):
				print("Fighting Sanders!")
			there_is_a_challenger = check_for_foes()
			if there_is_a_challenger:
				if character['Current Level'] == 1:
					print("Fighting Hens")
				elif character['Current Level'] == 2:
					print("Fighting Silkies")
				else:
					print("Fighting Roosters")
				# If level 1:
				#   combat(character, hen)
				# elif level 2:
				#   combat(character, silkie)
				# else:
				#   combat(character, rooster)
				print(f"The current character level is: Level {character['Current Level']}")

			#   if character_has_leveled():
			#       execute_glow_up_protocol()
			achieved_goal = check_if_goal_attained(character)
		else:
			# Add story elements to this, from planning documents
			print("Nice try, but that direction isn't valid! Please try again.")

	if character["Current HP"] > 0:
		# Add story elements to this, from planning documents
		print("Congrats on getting to the end! You win!")
		return None
	else:
		# Add story elements to this, from planning documents
		print("Sorry you didn't survive the game! Better luck next time.")


def main():
	"""
	Drive the program
	"""
	game()


if __name__ == "__main__":
	main()
