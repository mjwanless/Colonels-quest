def make_board():
	"""
	A function that generates the map for the game.
	"""
	board_dictionary = {
		(row, column): f'You\'re in room ({row}, {column}); There is nothing but fine hardwood under your feet.'
		for row in
		range(0, 5) for
		column in range(0, 5)}
	board_dictionary.update(
		{(row, column): f'You\'re in room ({row}, {column});  There is nothing but fine hardwood under your feet.' for
		 row in range(0, 5) for
		 column in range(6, 11)})
	board_dictionary.update(
		{(row, column): f'You\'re in room ({row}, {column});  There is nothing but fine hardwood under your feet.' for
		 row in range(0, 5) for
		 column in range(12, 17)})
	board_dictionary.update(
		{(row, column): f'You\'re in room ({row}, {column});  There is nothing but fine hardwood under your feet.' for
		 row in range(1, 4) for
		 column in range(18, 20)})
	board_dictionary.update({(2, 5): f'You\'re in room ({2}, {5}): There is a magic barrier here; It resonates with '
	                                 f'a power before unknown. It will only open if you are level 2.'})
	board_dictionary.update({(2, 11): f'You\'re in room ({2}, {11}): There is a magic barrier here; It resonates '
	                                  f'with a power before unknown. It will only open if you are level 3.'})
	board_dictionary.update({(2, 17): f'You\'re in room ({2}, {17}): There is a magic barrier here; Beyond stands '
	                                  f'Colonel Sanders; Are you ready to complete this quest? Proceed if so.'})
	board_dictionary.update({(2, 20): f'You\'re in room ({2}, {20})'})
	board_dictionary.update({(2, 4): f'You\'re in room ({2}, {4}): There is a magic barrier here; It resonates with '
	                                 f'a power before unknown. It will only open if you are level 2.'})
	board_dictionary.update({(2, 10): f'You\'re in room ({2}, {10}): There is a magic barrier here; It resonates '
	                                  f'with a power before unknown. It will only open if you are level 3.'})

	return board_dictionary


def enemy_generator(enemy):
	if enemy == "hen":
		return make_hen()
	elif enemy == "silkie":
		return make_silkie()
	elif enemy == "rooster":
		return make_rooster()
	elif enemy == "sanders":
		return make_sanders()


def make_character():
	return {
		"X-coordinate": 0,
		"Y-coordinate": 2,
		"Current HP": 20,
		"Max HP": 20,
		"Current Mana": 70,
		"Max Mana": 70,
		"Exp": 0,
		"Exp Needed": 15,
		"Current Level": 1}


def make_hen():
	return {"name": "hen", "Current HP": 15, "Max HP": 15, "Exp Value": 2}


def make_silkie():
	return {"name": "silkie", "Current HP": 30, "Max HP": 30, "Exp Value": 3}


def make_rooster():
	return {"name": "rooster", "Current HP": 50, "Max HP": 50, "Exp Value": 5}


def make_sanders():
	return {"name": "sanders", "Current HP": 100, "Max HP": 100, "Exp Value": 0}
