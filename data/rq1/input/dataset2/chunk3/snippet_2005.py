#Source: https://stackoverflow.com/questions/73821647/why-does-newdeck-pop0-give-an-attribute-error
for i in range(2):
    drawnCard = newDeck.pop(0)
    playerList.append(drawnCard)
    if (drawnCard[:1] == "J" or drawnCard[:1] == "Q" or drawnCard[:1] == "K"):
        playerSum += 10
    elif (drawnCard[:1] == "A"):
        playerSum += 11
    elif ((drawnCard[:2]) == "10"):
        playerSum += 10
    else:
        playerSum += int(drawnCard[:1])