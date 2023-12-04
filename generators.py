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
		"Current HP": 20,
		"Max HP": 20,
		"Current Mana": 100,
		"Max Mana": 100,
		"Exp": 0,
		"Exp Needed": 15,
		"Current Level": 1}





def make_hen():
	return {"name": "hen", "Current HP": 15, "Max HP": 15, "Exp Value": 10}


def make_silkie():
	return {"name": "silkie", "Current HP": 30, "Max HP": 30, "Exp Value": 3}


def make_rooster():
	return {"name": "rooster", "Current HP": 50, "Max HP": 50, "Exp Value": 0}


def make_sanders():
	return {"name": "Colonel Sanders", "Current HP": 100, "Max HP": 100, "Exp Value": 0}

