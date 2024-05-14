#Source: https://stackoverflow.com/questions/61537231/what-could-cause-this-error-filenotfounderror-errno-2-no-such-file-or-direc
import pathlib

directory = pathlib.Path('/Users/karl/files/Code')

stats ={}

for path in directory.iterdir():
    file = open(str(path))
    text = file.read().lower()

    punctuation  = (";", ".")
    for mark in punctuation:
        text = text.replace(mark, "")


    for word in text.split:
        if word in stats:

            stats[word] = stats[word] + 1
        else:
            stats[word] = 1

most_used_word = None
score_max = 0
for word, score in stats.items():
    if score > score_max:
        score_max = score
        most_used_word = word

print(word,"The most used word is : ", score_max) 