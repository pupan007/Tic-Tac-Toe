def player_turn(counter):
    if counter % 2 == 0:
        print("Player 1 turn ")
        player_char = "x"
        return player_char
    else:
        print("Player 2 turn ")
        player_char = "o"
        return player_char


def position_checker(cord_x, cord_y, grid):
    if grid[cord_x][cord_y] == "x" or grid[cord_x][cord_y] == "o":
        return False
    else:
        return True


def win_conditions(grid):
    def win_checker(temp_string):
        if temp_string == "xxx":
            string = "Player 1 won"
            print(string)
            return True
        elif temp_string == "ooo":
            string = "Player 2 won"
            print(string)
            return True

    #unpacking grid
    checked_string = ""
    for sublist in grid:
        for char in sublist:
            checked_string += char


    #horizontal check
    index = 0
    for counter in range(0, 3):
        temp_string = ""
        for counter2 in range(0, 3):
            temp_string += checked_string[index]
            index += 1
        if win_checker(temp_string):
            return True

    #vertical check
    for counter in range(0, 3):
        temp_string = ""
        temp_index = counter
        for counter2 in range(0, 3):
            temp_string += checked_string[temp_index]
            temp_index += 3
        if win_checker(temp_string):
            return True

    #diagonal check left to right
    temp_string = ""
    for counter in range(0, 3):
        temp_index = counter
        temp_index *= 4
        temp_string += checked_string[temp_index]
    if win_checker(temp_string):
        return True
    #diagonal heck right to left
    for counter in range(0, 3):
        temp_string = ""
        temp_index = 2
        for counter2 in range(0, 3):
            temp_string += checked_string[temp_index]
            temp_index += 2
        if win_checker(temp_string):
            return True
