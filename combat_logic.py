import generators


def combat(character, enemy):
	if enemy == "hen":
		enemy = generators.make_hen()
	elif enemy == "silkie":
		enemy = generators.make_silkie()
	elif enemy == "rooster":
		enemy = generators.make_rooster()
	else:
		enemy = generators.make_sanders()

	while character["Current HP"] > 0 and enemy["Current HP"] > 0:
		print(f"Combat is happening between the character and a {enemy['name']}.")
		return None
