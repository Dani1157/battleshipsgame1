import random
import time
import os

"""
    -------BATTLESHIPS-------
    How it will work:
    1. A 10x10 grid will have 8 ships of variable length randomly placed about.
    2. You will have 50 bullets to take down the ships that are placed down.
    3. You can choose a row and column such as A3 to indicate where to shoot.
    4. For every shot that hits or misses it will show up in the grid.
    5. A ship cannot be placed diagonally, so if a shot hits, the rest of
       the ship is in one of 4 directions: left, right, up, or down.
    6. If all ships are unearthed before using up all bullets, you win;
       else, you lose.

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""

# Global Variables
grid = []
grid_size = 10
num_of_ships = 8
bullets_left = 50
game_over = False
num_of_ships_sunk = 0
ship_positions = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    global grid, ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break

    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    global grid_size

    start_row, end_row = row, row + 1
    start_col, end_col = col, col + 1

    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_grid():
    global grid, grid_size, num_of_ships, ship_positions

    random.seed(time.time())

    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    num_of_ships_placed = 0
    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, grid_size - 1)
        random_col = random.randint(0, grid_size - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(
            random_row, random_col, direction, ship_size
        ):
            num_of_ships_placed += 1


def print_grid(debug_mode=False):
    global grid, alphabet

    print("   " + " ".join(str(i) for i in range(grid_size)))

    for row in range(len(grid)):
        print(f"{alphabet[row]} ", end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O" and not debug_mode:
                print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")


def accept_valid_bullet_placement():
    global alphabet, grid
    while True:
        placement = input(
            "Enter row (A-J) and column (0-9) such as A3: "
        ).upper()
        if len(placement) != 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row, col = placement[0], placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Enter letter (A-J) for row and (0-9) for column")
            continue
        row = alphabet.find(row)
        if (row == -1 or
            not (0 <= row < grid_size) or
                not (0 <= int(col) < grid_size)):
            print("Error: Invalid row or column, please enter again")
            continue
        col = int(col)
        if grid[row][col] in ("#", "X"):
            print("You have already shot a bullet here, pick somewhere else")
            continue
        return row, col


def check_for_ship_sunk(row, col):
    global ship_positions, grid

    for position in ship_positions:
        start_row, end_row, start_col, end_col = position
        if start_row <= row < end_row and start_col <= col < end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
            return True
    return False


def shoot_bullet():
    global grid, num_of_ships_sunk, bullets_left

    row, col = accept_valid_bullet_placement()
    print("\n----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            num_of_ships_sunk += 1
        else:
            print("A ship was shot")

    bullets_left -= 1


def check_for_game_over():
    global num_of_ships_sunk, num_of_ships, bullets_left, game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congrats, you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    global game_over
    clear_terminal()  # Clear terminal before each turn
    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while not game_over:

        print_grid(debug_mode=False)
        print("If you would like to change the grid")
        print("go into the code and Change one of the variables.")
        print("It is the same with the bullets")
        print(f"Number of ships remaining: {num_of_ships - num_of_ships_sunk}")
        print(f"Number of bullets left: {bullets_left}")
        shoot_bullet()
        print("----------------------------")
        check_for_game_over()

    print_grid(debug_mode=False)  # Show final grid after game over


if __name__ == '__main__':
    main()
