#Source: https://stackoverflow.com/questions/71628072/i-am-getting-the-error-filenotfounderror-errno-2-no-such-file-or-directory
print("Dictionary File Path -")
filename = input()

print("Words Length -")
word_length = input()
words = list()

with open(filename) as dict:
    for line in dict:
        if len(line) == word_length:
            list.append(line)
    print(words)