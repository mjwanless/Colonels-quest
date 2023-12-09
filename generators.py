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
	"""
    Generate an enemy, based on the input string name.

	:param enemy: a string representing the enemy's name
	:precondition: enemy is a string
	:postcondition: the returned values is an object, based on the string input name
	:return: a dictionary that represents an enemy character

    >>> enemy_generator("hen")
    {'name': 'hen', 'Current HP': 20, 'Max HP': 20, 'Exp Value': 2}

    >>> enemy_generator("silkie")
    {'name': 'silkie', 'Current HP': 35, 'Max HP': 35, 'Exp Value': 3}

    >>> enemy_generator("rooster")
    {'name': 'rooster', 'Current HP': 50, 'Max HP': 50, 'Exp Value': 5}

    >>> enemy_generator("sanders")
    {'name': 'sanders', 'Current HP': 100, 'Max HP': 100, 'Exp Value': 0}
    """
	if enemy == "hen":
		return make_hen()
	elif enemy == "silkie":
		return make_silkie()
	elif enemy == "rooster":
		return make_rooster()
	elif enemy == "sanders":
		return make_sanders()


def make_character():
	"""
	Generate the character object.

	:postcondition: the returned object represents the character's stats.
	:return: a dictionary that represents an player character

	>>> make_character()
	{'X-coordinate': 0, 'Y-coordinate': 2, 'Current HP': 20, 'Max HP': 20, 'Current Mana': 70, 'Max Mana': 70, 'Exp': 0, 'Exp Needed': 15, 'Current Level': 1}

	"""
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
	"""
	Generate the hen object.

	:postcondition: the returned object represents the stats that a hen enemy has.
	:return: a dictionary that represents a hen enemy

	>>> make_hen()
	{'name': 'hen', 'Current HP': 20, 'Max HP': 20, 'Exp Value': 2}
	"""
	return {"name": "hen", "Current HP": 20, "Max HP": 20, "Exp Value": 2}


def make_silkie():
	"""
	Generate the silkie object.

	:postcondition: the returned object represents the stats that a silkie enemy has.
	:return: a dictionary that represents a silkie enemy

	>>> make_silkie()
	{'name': 'silkie', 'Current HP': 35, 'Max HP': 35, 'Exp Value': 3}
	"""
	return {"name": "silkie", "Current HP": 35, "Max HP": 35, "Exp Value": 3}


def make_rooster():
	"""
	Generate the rooster object.

	:postcondition: the returned object represents the stats that a rooster enemy has.
	:return: a dictionary that represents a rooster enemy

	>>> make_rooster()
	{'name': 'rooster', 'Current HP': 50, 'Max HP': 50, 'Exp Value': 5}
	"""
	return {"name": "rooster", "Current HP": 50, "Max HP": 50, "Exp Value": 5}


def make_sanders():
	"""
	Generate the sanders boss object.

	:postcondition: the returned object represents the stats that colonel sanders has.
	:return: a dictionary that represents colonel sanders

	>>> make_sanders()
	{'name': 'sanders', 'Current HP': 100, 'Max HP': 100, 'Exp Value': 0}
	"""
	return {"name": "sanders", "Current HP": 100, "Max HP": 100, "Exp Value": 0}
