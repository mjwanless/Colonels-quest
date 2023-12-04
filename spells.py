import random


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
