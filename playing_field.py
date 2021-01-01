def empty_playing_field():
    # plot of empty field
    empty_grid = []
    rows = 3
    columns = 3
    for x in range(0, columns):
        empty_grid.append(["_"] * rows)
    return empty_grid


def plot_field(grid):
    print("  0 1 2")
    for column in range(0, 3):
        print(column, end=" ")
        for row in range(0, 3):
            print(grid[column][row], end=" ")
        print()


def temp_grid(game_char, re_column, re_row, grid):
    new_grid = grid
    new_grid[re_column][re_row] = game_char
    return new_grid
