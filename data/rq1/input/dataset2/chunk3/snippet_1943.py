#Source: https://stackoverflow.com/questions/50146402/why-is-this-nameerror-happening
import urllib


def read_text():
    quotes = open("C:\\Udacity Python\\Lesson 4\\movie_quotes.txt", "r")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)


read_text()


def check_profanity(contents_of_file):
    text_to_check = read_text.contents_of_file
    connection = urllib.urlopen(
        "http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()


check_profanity()