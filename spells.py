import random


def holy_blast(character: dict) -> int:
	"""
	Perform an attack (holy blast) based on the character's current level.

	A function that takes in a character dictionary and generates a return value based upon the character level,
	multiplied by random numbers generated between 1 and 4.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level value
	:postcondition: the return value is an integer that represents the damage dealt by the character's attack
	:return: an integer representing the damage dealt by the character's attack

	>>> random.seed(29)
	>>> character_1 = {"Current Level": 3}
	>>> holy_blast(character_1)
	7

	>>> character_2 = {"Current Level": 2}
	>>> holy_blast(character_2)
	4

	"""
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.randint(1, 4)

	return damage_sum


def smite(character: dict) -> int:
	"""
	Perform an attack (smite) based on the character's current level.

	A function that takes in a character dictionary and generates a return value based upon the character level,
	multiplied by random numbers generated between 2 and 7.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level value
	:postcondition: the return value is an integer that represents the damage dealt by the character's attack
	:return: an integer representing the damage dealt by the character's attack

	>>> random.seed(29)
	>>> character_1 = {"Current Level": 3, "Current Mana": 30}
	>>> smite(character_1)
	12

	>>> character_2 = {"Current Level": 2, "Current Mana": 30}
	>>> smite(character_2)
	12

	"""
	character["Current Mana"] -= 15
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.randint(2, 7)

	return damage_sum


def feather_throw() -> int:
	"""
	Perform an attack (feather throw) by an enemy.

	A function that randomly generates an integer by summing the random outputs of anywhere between 2 and 4 rolls of
	1 to 3 integers. This acts as a damage function for an enemy attack to the character.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> feather_throw()
	9

	>>> feather_throw()
	6

	"""
	damage_sum = 0
	for attack in range(random.randint(2, 4)):
		damage_sum += random.randint(1, 3)

	return damage_sum


def flavour_blast() -> int:
	"""
	Perform an attack (flavour blast) by an enemy.

	A function that randomly generates an integer between 1 and 20, and returns a damage integer based upon a range
	of if statements that are tied to the randomly generated number.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> flavour_blast()
	15

	>>> flavour_blast()
	4

	"""
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


def talons() -> int:
	"""
	Perform an attack (talons) by an enemy.

	A function that randomly generates three integers, from a selection of 2, 4, and 6, and sums them together. Then,
	the function returns that damage integer.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> talons()
	12

	>>> talons()
	16

	"""
	damage_sum = 0
	for attack in range(3):
		damage_sum += random.choice((2, 4, 6))

	return damage_sum


def deep_fry() -> int:
	"""
	Perform an attack (deep fry) by an enemy.

	A function that randomly generates an integer between 5 and 10 then the function returns that damage integer.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> deep_fry()
	9

	>>> deep_fry()
	5

	"""
	return random.randint(5, 10)


def herbs_and_spices() -> int:
	"""
	Perform an attack (herbs and spices) by an enemy.

	A function that randomly generates 11 integers between 0 and 2 and then sums them together. Then the function
	returns that damage integer.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> herbs_and_spices()
	13

	>>> herbs_and_spices()
	8

	"""
	damage_sum = 0
	for attack in range(11):
		damage_sum += random.randint(0, 2)

	return damage_sum


def plumage() -> int:
	"""
	Perform a heal (plumage) by an enemy.

	A function that randomly generates an integer between 1 and 5 then the function returns that healing integer.

	:postcondition: the return value is an integer that represents the damage healed by the enemy's roll
	:return: an integer representing the damage healed by the enemy's roll

	>>> random.seed(29)
	>>> plumage()
	5

	>>> plumage()
	1

	"""
	return random.randint(1, 5)


def scratch() -> int:
	"""
	Perform an attack (scratch) by an enemy.

	A function that randomly generates an integer between 1, 2, 3, or 4 then the function returns that damage integer.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> scratch()
	1

	>>> scratch()
	3

	"""
	return random.choice((1, 2, 3, 4))


def peck() -> int:
	"""
	Perform an attack (peck) by an enemy.

	A function that randomly generates an integer between 2, 4, and 6 then the function returns that damage integer.

	:postcondition: the return value is an integer that represents the damage dealt by the enemy's attack
	:return: an integer representing the damage dealt by the enemy's attack

	>>> random.seed(29)
	>>> peck()
	6

	>>> peck()
	2

	"""
	return random.choice((2, 4, 6))


def judgment(character: dict) -> int:
	"""
	Perform an attack (judgment) based on the character's current level.

	A function that takes in a character dictionary and generates a return value based upon the character level,
	multiplied by random integers, selected from 0, 2, 4, 6, and 8.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level value
	:postcondition: the return value is an integer that represents the damage dealt by the character's attack
	:return: an integer representing the damage dealt by the character's attack

	>>> random.seed(29)
	>>> character_1 = {"Current Level": 3, "Current Mana": 30}
	>>> judgment(character_1)
	12

	>>> character_2 = {"Current Level": 2, "Current Mana": 30}
	>>> judgment(character_2)
	16

	"""
	character["Current Mana"] -= 30
	damage_sum = 0
	for attack in range(character["Current Level"]):
		damage_sum += random.choice((0, 2, 4, 6, 8))

	return damage_sum


def breading() -> int:
	"""
	Perform a healing move (breading) by an enemy.

	A function that randomly generates an integer between 2 and 18 then the function returns that healing integer.

	:postcondition: the return value is an integer that represents the damage healed by the enemy's roll
	:return: an integer representing the damage healed by the enemy's roll

	>>> random.seed(29)
	>>> breading()
	12

	>>> breading()
	12

	"""
	heal_sum = 0
	for attack in range(random.randint(1, 3)):
		heal_sum += random.randint(2, 6)

	return heal_sum


def heal(character: dict) -> int:
	"""
	Perform a healing move based on the character's current level.

	A function that takes in a character dictionary and generates a return value based upon the character level,
	multiplied by random integers, selected from a range of 3 to 10.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level value
	:postcondition: the return value is an integer that represents the damage healed by the character's roll
	:return: an integer representing the damage healed by the character's random roll

	>>> random.seed(29)
	>>> character_1 = {"Current Level": 3, "Current Mana": 30}
	>>> heal(character_1)
	19

	>>> character_2 = {"Current Level": 2, "Current Mana": 30}
	>>> heal(character_2)
	12

	"""
	character["Current Mana"] -= 20
	heal_sum = 0
	for attack in range(character["Current Level"]):
		heal_sum += random.randint(3, 10)

	return heal_sum


def regen_mana(character: dict):
	"""
	Regenerate mana each turn after player commits to an attack.

	A function that modifies and increases the value of the character's "Current Mana" value by 7 + 2 * the
	character's level.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level value and both Mana values (Max and Current)
	:postcondition: the character's current mana is increased between 8 and 10 per turn

	>>> random.seed(29)
	>>> character_1 = {"Current Level": 1, "Current Mana": 30, "Max Mana": 200}
	>>> regen_mana(character_1)
	>>> character_1["Current Mana"]
	39

	>>> character_2 = {"Current Level": 3, "Current Mana": 30, "Max Mana": 200}
	>>> regen_mana(character_2)
	>>> character_2["Current Mana"]
	43

	"""
	character["Current Mana"] += 7 + character["Current Level"] * 2
	if character["Current Mana"] > character["Max Mana"]:
		character["Current Mana"] = character["Max Mana"]


def post_fight_heal(character: dict):
	"""
	Regenerate mana and health after each combat encounter ends.

	A function that modifies and increases the value of the character's "Current Mana" value by 10 and the
	character's "Current HP" value by 5. It calls balance() at the end of the modifiers, which stops the current
	mana or health from increasing past the maximum value.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level, Current Mana, and Current HP values
	:postcondition: the character's current mana is increased by 10 and current hp is increased by 5

	>>> random.seed(29)
	>>> character_1 = {"Current HP": 20, "Max HP": 20, "Current Mana": 70, "Max Mana": 70}
	>>> post_fight_heal(character_1)
	>>> character_1["Current Mana"]
	70
	>>> character_1["Current HP"]
	20

	>>> character_2 = {"Current HP": 20, "Max HP": 120, "Current Mana": 50, "Max Mana": 170}
	>>> post_fight_heal(character_2)
	>>> character_2["Current Mana"]
	60
	>>> character_2["Current HP"]
	25
	"""
	character["Current Mana"] += 10
	character["Current HP"] += 5
	balance(character)


def balance(character: dict):
	"""
	Balance the character's current health and mana values to not exceed the maximum character value.

	A function that takes the character's max and current mana and HP and checks the value of the current mana and hp
	against their relative maximums. If the current values exceed the maximums, it is set to them instead.

	:param character: a character dictionary
	:precondition: character is a dictionary with a level, Current/Max Mana, and Current/Max HP values
	:postcondition: the character's current mana is equal to, or less than the maximum and current hp is equal to, or
	less than the maximum

	>>> random.seed(29)
	>>> character_1 = {"Current HP": 20, "Max HP": 20, "Current Mana": 70, "Max Mana": 70}
	>>> balance(character_1)
	>>> character_1["Current Mana"]
	70
	>>> character_1["Current HP"]
	20

	>>> character_2 = {"Current HP": 220, "Max HP": 120, "Current Mana": 250, "Max Mana": 170}
	>>> balance(character_2)
	>>> character_2["Current Mana"]
	170
	>>> character_2["Current HP"]
	120
	"""
	if character["Current Mana"] > character["Max Mana"]:
		character["Current Mana"] = character["Max Mana"]
	if character["Current HP"] > character["Max HP"]:
		character["Current HP"] = character["Max HP"]
