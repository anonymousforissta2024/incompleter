#Source: https://stackoverflow.com/questions/49971390/valueerror-not-enough-values-to-unpack-expected-3-got-2-typeerror-must-be
# Team manager welcome screen, date & time
print("Welcome to San Angelo's Softball Team Roster")
print("This program keeps the most up-to-date information")
print("Today's Date: April 23, 2018")
print("Current Time: 0900\n")

# Create a dictionary named "team_members"
team_members = {}

# Provides Menu Screen
menu_selection = print_menu()

# Create while loop repeating the main menu.
while menu_selection != 9:

    if menu_selection == 1:
        print_members(team_members)

    elif menu_selection == 2:
        team_members = add_members(team_members)

    elif menu_selection == 3:
        team_members = remove_members(team_members)

    elif menu_selection == 4:
        team_members = edit_members(team_members)

    elif menu_selection == 5:
        filename = input("Enter Desired Filename: ")
        save_members(team_members, filename)

    elif menu_selection == 6:
        filename = input("Enter Existing Filename: ")
        load_members(team_members, filename)

    menu_selection = print_menu()

print("Thank You For Updating San Angelo's Softball Team Roster!")