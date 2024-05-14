#Source: https://stackoverflow.com/questions/61939039/typeerror-username-object-is-not-iterable-in-python3
import os
import sys

class usernames(object):
    def __init__(self, filename: str):
        self.filename = filename
        self.words = self.file_to_text

    def file_to_text(self):
        with open(self.filename, "r") as f:
            name_list = [line.rstrip() for line in f]

        return name_list


def main():
    user_files = []

    if os.path.isfile(sys.argv[1]):
        filename = os.path.splitext(sys.argv[1])[-1].lower()
        if filename.endswith('.txt'):
            user_files.append(sys.argv[1])

    for files in user_files:
        test_name = usernames(files)
        print(test_name)
    for test in test_name:
        print(test)


if __name__ == '__main__':
    main()