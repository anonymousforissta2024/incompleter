#Source: https://stackoverflow.com/questions/54777002/i-need-assistance-with-a-typeerror-in-python-3-im-new-to-coding-python-so-im-a-l
player_pos = [x,y]

screen.fill(background_color)
if enemy_pos[1] >= 0 and enemy_pos[1] < height:
    enemy_pos[1] += 15
else:
    enemy_pos[1] = 0