#Source: https://stackoverflow.com/questions/56308858/typeerror-not-supported-between-instances-of-int-and-str-and-del-from-l
player_score = 3000
with open('testscores.txt', 'r') as f:
    for line in f:
        highscores = line.split(",")
    highscores.append(player_score)
    lowest_score = int(highscores[0])
    for i in range (1, len(highscores)):
        if int(highscores[i]) < int(lowest_score):
            lowest_score = highscores[i]
    lowest_score = int(lowest_score)
    del highscores[lowest_score]
    highhelper = ''
    for i in range (0, len(highscores)-1):
        highhelper += str(highscores[i])+","
    highhelper += str(highscores[len(highscores)-1])
    print(highhelper)
    with open('testscores.txt', 'w') as outF:
        outF.write(str(highhelper))
    print("kicking out score: "+str(lowest_score))