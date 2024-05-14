#Source: https://stackoverflow.com/questions/28121499/typeerror-function-object-is-not-subscriptable-python
def scorekeeper():
    Scorekeeper = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return Scorekeeper

def addscore(Scorekeeper):
    Addscore = int(input("what player scored a goal?"))
    Addscore = Addscore - 1 
    (Scorekeeper[Addscore]) = ((Scorekeeper[Addscore]) + 1) 
    return Scorekeeper
def histogram(Scorekeeper):
    print("\nCreating a histogram from values: ")
    print("%s %10s %10s" %("Element", "Ranking", "Histogram"))
    for i in range(len(Scorekeeper)):
        print("%7d%5d %-s" % (i +1, Scorekeeper[i], "*" * Scorekeeper[i])) 
def main():
    Scorekeeper = scorekeeper()
    endgame = 'n'
    while endgame == 'n':
        Addscore = addscore(scorekeeper)
        endgame = input("Has the game ended? y/n")

    histogram(scorekeeper)

main()