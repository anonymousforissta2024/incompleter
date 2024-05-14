#Source: https://stackoverflow.com/questions/50557518/getting-nameerror-name-room-path-is-not-defined
def room():
    room_path=["1","2"]
    user_choice = ""

print ("If you decide to ditch Todd and go to the campfire alone, enter 1")
print ("If you decide to drag Todd with you to the campfire, enter 2")
user_choice = input("your option number")

if user_choice == room_path [1]:
    print ("yes")
elif user_choice == room_path [2]:
    print ("no")