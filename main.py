import playing_field as pf
import game_handler as gh

#innit
counter = 0
print("Game started!")
pf.plot_field(pf.empty_playing_field())
temp_grid = pf.empty_playing_field()

#game
while counter != 9:
    gh.player_turn(counter)
    try:
        x_cord = int(input("Cord X?> "))
        y_cord = int(input("Cord Y?> "))
        if gh.position_checker(x_cord, y_cord, temp_grid):
            temp_grid = pf.temp_grid(gh.player_turn(counter), x_cord, y_cord, temp_grid)
            counter += 1
            pf.plot_field(temp_grid)
            if gh.win_conditions(temp_grid):
                break
        else:
            print("Cord already taken")
            pf.plot_field(temp_grid)
            continue
    except:
        print("You have to choose cord between 0-2")
        continue
