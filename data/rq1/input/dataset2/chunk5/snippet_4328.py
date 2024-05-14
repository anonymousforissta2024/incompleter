#Source: https://stackoverflow.com/questions/48822141/how-can-i-fix-this-type-error
for i, value in enumerate(line_score):
     print(i, value)
     if (value["GAME_SEQUENCE"] != game_sequence):
           game_sequence += 1