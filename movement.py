
def describe_current_location(board: dict, character: dict):
    """
    Describe the current location that the character is in.

    A function that takes in the current game board and the character object and returns a description of the current
    location, using the coordinates of the character and the description of the current location from the board object.

    :param board: a dictionary containing the current game board object
    :param character: a dictionary containing the current character object
    :precondition: board is a dictionary with location data, in tuple keys, with string descriptions
    :precondition: character is a dictionary with location data
    :postcondition: the printed string provides the current location of the character object on the board,
    represented as a mini-map

    """
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


def get_user_choice() -> int:
    """
    Receive user input and validate the selected direction so that it can work with the game board.

    A function that receives no input, but asks the user to input a direction. If the direction is valid, it returns
    the correct integer value. It will keep asking the user for input as long as the inputted value is not 1 to 4,
    inclusive. The direction is valid only if it is one of the four cardinal directions, represented by integer keys,
    and displayed to the user as a string.

    :postcondition: the returned integer value is between 1 and 4, inclusive
    :return: an integer value indicating one of the listed cardinal directions
    :raises ValueError: if user_input is not an integer
    """
    user_directions = {1: "north", 2: "east", 3: "south", 4: "west"}
    valid_user_input = False
    user_direction_input = 0

    while not valid_user_input:
        try:
            user_direction_input = int(input("Please input a direction of either 1. North, 2. East, 3. South, 4. West: "))
            if user_direction_input in user_directions:
                valid_user_input = True
            else:
                print("The direction provided doesn't exist in our system; Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return user_direction_input


def validate_move(board: dict, character: dict, direction: int) -> bool:
    """
    Determine whether a direction will extend past the edges of the game board and prevent invalid movement by the
    character if so.

    A function that takes in three arguments: the game board, the character, and a direction. The function will
    determine the current character's position on the board, and whether the passed in direction is a valid move for
    that character to make. If the move is valid, return True. If not, return False.

    :param board: a dictionary containing the current gameboard object
    :param character: a dictionary containing the current character object
    :param direction: an integer, between 1 and 4, inclusive, that represents the movement direction
    :precondition: board is a dictionary with location data, in tuple keys, with string descriptions
    :precondition: character is a dictionary with location data, and a health key:value pair
    :precondition: direction is an integer between 1 and 4
    :postcondition: the returned boolean indicates the validity of the movement on the board
    :return: a boolean value representing the validity of the movement direction

    >>> board_1 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
    ... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
    >>> character_1 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction_1 = 2
    >>> validate_move(board_1, character_1, direction_1)
    True
    >>> board_2 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
    ... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
    >>> character_2 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction_2 = 4
    >>> validate_move(board_2, character_2, direction_2)
    False
    >>> board_3 = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
    ... (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
    >>> character_3 = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> direction_3 = 3
    >>> validate_move(board_3, character_3, direction_3)
    False
    """
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


def move_character(character: dict, direction: int):
    """
    Move the character to a new location on the board.

    A function that takes in a character dictionary and a direction value. The character's X, or Y coordinate values
    are modified by +1 or -1, depending on which direciton value is passed into the function.

    :param character: a dictionary containing the current character object
    :param direction: an integer, between 1 and 4, inclusive, that represents the movement direction
    :precondition: character is a dictionary with location data, and a health key:value pair
    :precondition: direction is an integer between 1 and 4
    :postcondition: the character object has a modified X, or Y coordinate value that indicates their new position on
    the board

    >>> character_1 = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction_1 = 2
    >>> move_character(character_1, direction_1)
    >>> print(character_1)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> character_2 = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 5}
    >>> direction_2 = 3
    >>> move_character(character_2, direction_2)
    >>> print(character_2)
    {'X-coordinate': 2, 'Y-coordinate': 4, 'Current HP': 5}
    >>> character_3 = {'X-coordinate': 1, 'Y-coordinate': 3, 'Current HP': 5}
    >>> direction_3 = 1
    >>> move_character(character_3, direction_3)
    >>> print(character_3)
    {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    """
    if direction == 1:
        character["Y-coordinate"] -= 1
    elif direction == 2:
        character["X-coordinate"] += 1
    if direction == 3:
        character["Y-coordinate"] += 1
    elif direction == 4:
        character["X-coordinate"] -= 1


def check_if_goal_attained(character: dict) -> bool:
    """
    Check to see if the character has reached the goal, or the designated spot on the board.

    A function that takes in a character object, and checks the goal tuple value of the map goal coordinates against
    the current value of the character's X, and Y coordinate values. If so, return a True boolean value. If not,
    return False.

    :param character: a dictionary containing the current character object
    :precondition: character is a dictionary with location data, and a health key:value pair
    :postcondition: the return value is a boolean that represents whether the character has reached a specific spot on
    the board
    :return: a boolean value representing whether the character has reached the end goal

    >>> character_1 = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> check_if_goal_attained(character_1)
    False
    >>> character_2 = {'X-coordinate': 20, 'Y-coordinate': 2, 'Current HP': 5}
    >>> check_if_goal_attained(character_2)
    True
    """
    return (character["X-coordinate"], character["Y-coordinate"]) == (20, 2)
