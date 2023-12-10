import random
import time
import generators
import spells


def level_up(character: dict):
    """
    Perform level-up actions for the given character, updating various attributes and displaying character stats.

    This function increments the character's level by 1 and adjusts several attributes such as experience points,
    health points, mana points, and their corresponding maximum values. It then calls the balance function to
    ensure that the current values don't exceed the maximum.

    :param character: a dictionary representing the characters attributes
    :precondition: character must be a dictionary containing the required attributes
    :postcondition: The character's level, experience points, health points, and mana points are updated

    >>> test_character = {'Current Level': 2, 'Exp': 15, 'Exp Needed': 35, 'Max HP': 30,
    ... 'Current HP': 25, 'Max Mana': 50, 'Current Mana': 40}
    >>> level_up(test_character)
    >>> print(test_character)
    {'Current Level': 3, 'Exp': 0, 'Exp Needed': 55, 'Max HP': 45, 'Current HP': 45, 'Max Mana': 75, 'Current Mana': 75}
    """
    character["Current Level"] += 1
    character["Exp"] = 0
    character["Exp Needed"] += 20
    character["Max HP"] += 15
    character["Current HP"] = character["Max HP"]
    character["Max Mana"] += 25
    character["Current Mana"] = character["Max Mana"]
    spells.balance(character)


def generate_enemy(enemy: str) -> dict:
    """
    Generate an enemy based on the specified type.

    This function takes a string representing the type of enemy to generate. Depending on the specified type, it calls
    the appropriate function from the generators.py module to create and return a dictionary representing the enemy.

    :param enemy: a string representing the type of enemy to generate
    :precondition: enemy is a string with a valid enemy type
    :postcondition: a dictionary representing the generated enemy
    :return: a dictionary

    >>> generate_enemy("hen")
    {'name': 'hen', 'Current HP': 15, 'Max HP': 15, 'Exp Value': 2}

    >>> generate_enemy("silkie")
    {'name': 'silkie', 'Current HP': 25, 'Max HP': 25, 'Exp Value': 3}

    >>> generate_enemy("rooster")
    {'name': 'rooster', 'Current HP': 40, 'Max HP': 40, 'Exp Value': 5}

    >>> generate_enemy("sanders")
    {'name': 'sanders', 'Current HP': 125, 'Max HP': 125, 'Exp Value': 0}
    """
    if enemy == "hen":
        return generators.make_hen()
    elif enemy == "silkie":
        return generators.make_silkie()
    elif enemy == "rooster":
        return generators.make_rooster()
    elif enemy == "sanders":
        return generators.make_sanders()


def print_stats(character: dict, enemy: dict):
    """
    Prints the character's stats along with the enemy's.

    :param character: a dictionary representing the characters attributes
    :param enemy: a dictionary representing the characters attributes
    :precondition: character must be a dictionary containing the required attributes
    :precondition: enemy must be a dictionary containing the required attributes
    :postcondition: a printout of both sets of stats is printed to the console
    """
    print(f"""
            ==================================
            Character Stats:        HP: {character['Current HP']}/{character['Max HP']}
                                    Mana: {character['Current Mana']}/{character['Max Mana']}
            ----------------------------------
            {enemy['name']} Stats:              HP {enemy['Current HP']}/{enemy['Max HP']}
            ==================================	
            """)


def print_spells(character: dict):
    """
    Prints the character's spells and selection options.

    :param character: a dictionary representing the characters attributes
    :precondition: character must be a dictionary containing the required attributes
    :postcondition: a printout of the character's options and spell information
    """
    print(f"""
    ================================================================================
    Your turn: What would you like to do? Type a number to cast that spell.

    1. Holy Blast  |  ({character["Current Level"]} * d6)             | Cost: 0 Mana
    2. Smite       |  ({character["Current Level"]} * d10)            | Cost: 15 Mana
    3. Judgment    |  ({character["Current Level"]} * (0, 4, or 8)))  | Cost: 30 Mana
    4. Heal        |  ({character["Current Level"]} * (3 - 10)))      | Cost: 20 Mana
    ================================================================================
    """)


def user_spell_choice(character: dict, enemy: dict, user_choice: int):
    """
    Choose a spell based on the user's input and send that damage/health to the correct recipient by calling the
    correct spell function.

    This function receives a character, an enemy, and the user's choice of spell as input. Depending on the
    user's choice, it calls the corresponding spell function from the 'spells' module, applies the spell's
    effects to the enemy and/or character, and prints a message describing the outcome.

    :param character: a dictionary representing the characters attributes
    :param enemy: a dictionary representing the characters attributes
    :param user_choice: an integer representing the choice that the user made
    :precondition: character must be a dictionary containing the required attributes
    :precondition: enemy must be a dictionary containing the required attributes
    :precondition: user_choice must be an integer between 1 and 4, inclusive
    :postcondition: the enemy's and/or character's attributes are updated based on the chosen spell
    """
    if user_choice == 1:
        damage = spells.holy_blast(character)
        enemy["Current HP"] -= damage
        print(f"You've done {damage} damage to {enemy['name']} with holy blast!")
    elif user_choice == 2 and character["Current Mana"] > 15:
        damage = spells.smite(character)
        enemy["Current HP"] -= damage
        print(f"You've done {damage} damage to {enemy['name']} with smite!")
    elif user_choice == 3:
        damage = spells.judgment(character)
        enemy["Current HP"] -= damage
        print(f"You've done {damage} damage to {enemy['name']} with judgment!")
    elif user_choice == 4:
        heal = spells.heal(character)
        character["Current HP"] += heal
        print(f"You've healed {heal} HP.")


def combat(character: dict, enemy: str):
    enemy = generate_enemy(enemy)

    peck_cooldown = 0
    feather_throw_cooldown = 0
    plumage_cooldown = 0
    talons_cooldown = 0
    herbs_and_spices_cooldown = 0
    breading_cooldown = 0
    flavour_blast_cooldown = 0

    print(f"Combat is happening between the character and a {enemy['name']}.")

    time.sleep(2)
    while character["Current HP"] > 0 and enemy["Current HP"] > 0:
        print_stats(character, enemy)

        while True:
            print_spells(character)

            try:
                user_choice = int(input("Make a choice from the above list: "))

                if 1 <= user_choice <= 4:
                    if (
                            (user_choice == 1) or
                            (user_choice == 2 and character["Current Mana"] >= 15) or
                            (user_choice == 3 and character["Current Mana"] >= 30) or
                            (user_choice == 4 and character["Current Mana"] >= 20)
                    ):
                        break
                    else:
                        print("Not enough mana to cast the selected spell. Please choose another.")
                else:
                    print("That's not a valid value; Please enter an int between 1 and 4, inclusive.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        time.sleep(1)
        user_spell_choice(character, enemy, user_choice)

        time.sleep(1)

        if enemy["Current HP"] <= 0:
            print(f"You've defeated the {enemy['name']}! ")
            spells.post_fight_heal(character)
            character["Exp"] += enemy["Exp Value"]
            print(f"You've gained {enemy['Exp Value']} xp. You have {character['Exp']} xp")
            break

        print(f"You've regenerated {7 + character['Current Level'] * 3} mana.")
        spells.regen_mana(character)

        spells.balance(character)

        time.sleep(1)

        print("It's now the enemy's turn.")

        if enemy["name"] == "hen":
            while True:
                abilities = random.choice(("peck", "scratch"))
                if abilities == "peck" and not peck_cooldown:
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with peck!")
                    peck_cooldown = 2
                    break
                if abilities == "scratch":
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with scratch!")
                    break

            if peck_cooldown > 0:
                peck_cooldown -= 1

        if enemy["name"] == "silkie":
            while True:
                abilities = random.choice(("peck", "scratch", "feather", "plumage"))
                if abilities == "peck" and not peck_cooldown:
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with peck!")
                    peck_cooldown = 2
                    break
                if abilities == "scratch":
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with scratch!")
                    break
                if abilities == "feather" and not feather_throw_cooldown:
                    damage = spells.feather_throw()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with feather throw!")
                    feather_throw_cooldown = 3
                    break
                if abilities == "plumage" and not plumage_cooldown:
                    heal = spells.plumage()
                    enemy["Current HP"] += heal
                    print(f"{enemy['name']} healed {heal} damage to themselves with plumage!")
                    plumage_cooldown = 2
                    break

            if peck_cooldown > 0:
                peck_cooldown -= 1
            if feather_throw_cooldown > 0:
                feather_throw_cooldown -= 1
            if plumage_cooldown > 0:
                plumage_cooldown -= 1

        if enemy["name"] == "rooster":
            while True:
                abilities = random.choice(("peck", "scratch", "feather", "plumage", "talons"))
                if abilities == "peck" and not peck_cooldown:
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with peck!")
                    peck_cooldown = 2
                    break
                if abilities == "scratch":
                    damage = spells.peck()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with scratch!")
                    break
                if abilities == "feather" and not feather_throw_cooldown:
                    damage = spells.feather_throw()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with feather throw!")
                    feather_throw_cooldown = 3
                    break
                if abilities == "plumage" and not plumage_cooldown:
                    heal = spells.plumage()
                    enemy["Current HP"] += heal
                    print(f"{enemy['name']} healed {heal} damage to themselves with plumage!")
                    plumage_cooldown = 2
                    break
                if abilities == "talons" and not talons_cooldown:
                    damage = spells.talons()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with talons!")
                    plumage_cooldown = 4
                    break

            if peck_cooldown > 0:
                peck_cooldown -= 1
            if feather_throw_cooldown > 0:
                feather_throw_cooldown -= 1
            if plumage_cooldown > 0:
                plumage_cooldown -= 1
            if talons_cooldown > 0:
                talons_cooldown -= 1

        if enemy["name"] == "sanders":
            while True:
                abilities = random.choice(("deep", "herbs", "breading", "flavour"))
                if abilities == "deep":
                    damage = spells.deep_fry()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with Deep fry!")
                    break
                if abilities == "herbs" and not herbs_and_spices_cooldown:
                    damage = spells.herbs_and_spices()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you 11 herbs and spices!")
                    peck_cooldown = 2
                    break
                if abilities == "breading" and not breading_cooldown:
                    heal = spells.breading()
                    enemy["Current HP"] += heal
                    print(f"{enemy['name']} healed {heal} damage to themselves with breading!")
                    breading_cooldown = 4
                    break
                if abilities == "flavour" and not flavour_blast_cooldown:
                    damage = spells.flavour_blast()
                    character["Current HP"] -= damage
                    print(f"{enemy['name']} did {damage} damage to you with flavour blast!")
                    plumage_cooldown = 3
                    break

            if herbs_and_spices_cooldown > 0:
                herbs_and_spices_cooldown -= 1
            if breading_cooldown > 0:
                breading_cooldown -= 1
            if flavour_blast_cooldown > 0:
                flavour_blast_cooldown -= 1

        time.sleep(1)

        if character["Current HP"] <= 0:
            print(f"Sorry; You've died to a {enemy['name']}")
