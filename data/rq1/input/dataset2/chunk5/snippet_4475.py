#Source: https://stackoverflow.com/questions/54361250/how-to-fix-this-nameerror-problem-in-python-3-6
filenames = [
    "The Wallypug in London.txt", 
    "Chats on Old Silver.txt", 
    "Jack Jingle, and Sucky Shingle.txt", 
    "Superstition and Force.txt"
]


def count_word(filename, word):
    with open(filename) as open_file:
        file_content = open_file.read()

    count_num = file_content.lower().count(word)
    return count_num


for filename in filenames:
    count_word(filename, "great")
    print('There are ' + str(count_num) + " 'great' in " + filename + ".")