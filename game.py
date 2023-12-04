"""
Malcolm Wanless
A01365553
"""
import itertools

import story
import random
import generators
import spells
import movement
import combat_logic


def check_for_foes():
	# Change this to a different value
	return True


def game():
	"""
	Drive the game
	"""
	board = generators.make_board()
	character = generators.make_character()
	achieved_goal = False
	# Put game story function here (just prints out the story)
	movement.describe_current_location(board, character)

	while not achieved_goal and character["Current HP"] > 0:
		direction = movement.get_user_choice()
		valid_move = movement.validate_move(board, character, direction)
		if valid_move:
			movement.move_character(character, direction)
			movement.describe_current_location(board, character)
			if (character["X-coordinate"], character["Y-coordinate"]) == (19, 2):
				combat_logic.combat(character, "sanders")
			there_is_a_challenger = check_for_foes()
			if there_is_a_challenger:
				if character['Current Level'] == 1:
					combat_logic.combat(character, "hen")
				elif character['Current Level'] == 2:
					print("Fighting Silkies")
					combat_logic.combat(character, itertools.cycle(["hen", "silkie"]))
				else:
					print("Fighting Roosters")
					combat_logic.combat(character, itertools.cycle(["hen", "silkie", "rooster"]))
			#   Here, you should have something like:
			#   if character["Exp"] >= character["Exp Needed"]:
			#       level_up()
			achieved_goal = movement.check_if_goal_attained(character)
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
