#Source: https://stackoverflow.com/questions/34029387/text-adventure-game-receives-attributeerror
import gamedata


if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

    # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
    # depending on whether or not it's been visited before,
    #   print either full description (first time visit) or brief description (every subsequent visit)

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        choice = input("\nEnter action: ")

        if (choice == "[menu]"):
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")