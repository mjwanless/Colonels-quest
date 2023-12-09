
def describe_current_location(board, character):
    """
    Describe the current location that the character is in.

    A function that takes in the current gameboard and the character object and returns a description of the current
    location, using the coordinates of the character and the description of the current location from the board object.

    :param board: a dictionary containing the current gameboard object
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


def get_user_choice():
    """
    Receive user input and validate the selected direction so that it can work with the game board.

    A function that receives no input, but asks the user to input a direction. If the direction is valid, it returns
    the correct integer value. It will keep asking the user for input as long as the inputted value is not 1 to 4,
    inclusive. The direction is valid only if it is one of the four cardinal directions, represented by integer keys,
    and displayed to the user as a string.

    :postcondition: the returned integer value is between 1 and 4, inclusive.
    :return: an integer value indicating one of the listed cardinal directions
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


def validate_move(board, character, direction):
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


def move_character(character, direction):
    if direction == 1:
        character["Y-coordinate"] -= 1
    elif direction == 2:
        character["X-coordinate"] += 1
    if direction == 3:
        character["Y-coordinate"] += 1
    elif direction == 4:
        character["X-coordinate"] -= 1


def check_if_goal_attained(character):
    return (character["X-coordinate"], character["Y-coordinate"]) == (20, 2)
