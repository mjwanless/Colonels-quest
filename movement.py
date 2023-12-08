
def describe_current_location(board, character):
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
