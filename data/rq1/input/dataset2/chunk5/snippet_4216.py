#Source: https://stackoverflow.com/questions/59614941/python-facebookchat-attributeerror-str-object-has-no-attribute-to-send-data
import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")