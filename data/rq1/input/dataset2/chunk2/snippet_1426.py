#Source: https://stackoverflow.com/questions/20126320/attribute-error-int-object-has-no-attribute-choice
while health_1 > 0 and health > 0 and stamina > 0:
    random = random.choice(accuracy)
    if random != "0":
        print("\n\n", random)
        print("\nYou manage to hit the creature for", dmg, "damage!")
        health_1 -= dmg
        stamina -= stam_loss
        print("The creature now has", health_1, "health")
        print("\nThe creature hits you for 1 damage!")
        health -= 1
        print("Health:", health, "Stamina:", stamina,) 