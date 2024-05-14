#Source: https://stackoverflow.com/questions/73666495/how-to-avoid-attributeerror-nonetype-object-has-no-attribute-text-webscrapi
import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://www.reddit.com/r/random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="_2yYPPW47QxD4lFQTKpfpLQ").text ## this is supposed to get the title of the subreddit and this is where my error is occurring

    print(f"{title} \nSelect this subreddit? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        url = "https://www.reddit.com/%s" % title ## Some issue, not sure what
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break