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
	story.story_intro()
	movement.describe_current_location(board, character)

	while not achieved_goal and character["Current HP"] > 0:
		direction = movement.get_user_choice()
		valid_move = movement.validate_move(board, character, direction)
		if valid_move:
			movement.move_character(character, direction)
			movement.describe_current_location(board, character)
			if (character["X-coordinate"], character["Y-coordinate"]) == (19, 2):
				story.story_sanders()
				combat_logic.combat(character, "sanders")
			if not (character["X-coordinate"], character["Y-coordinate"]) == (20, 2):
				there_is_a_challenger = check_for_foes()
				if there_is_a_challenger:
					if character['Current Level'] == 1:
						combat_logic.combat(character, "hen")
					elif character['Current Level'] == 2:
						combat_logic.combat(character, itertools.cycle(["hen", "silkie"]))
					else:
						combat_logic.combat(character, itertools.cycle(["hen", "silkie", "rooster"]))
				if character["Current Level"] < 4:
					if character["Exp"] >= character["Exp Needed"]:
						combat_logic.level_up(character)
					if character["Current Level"] == 2:
						story.story_level_2()
					if character["Current Level"] == 3:
						story.story_level_3()
				achieved_goal = movement.check_if_goal_attained(character)
			else:
				break
		else:
			print("Nice try, but that direction isn't valid! Please try again.")

	if character["Current HP"] > 0:
		story.story_end_of_game()
		print("Congrats on getting to the end! You win!")
		return None
	else:
		story.story_character_death()


def main():
	"""
	Drive the program
	"""
	game()


if __name__ == "__main__":
	main()
