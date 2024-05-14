#Source: https://stackoverflow.com/questions/51733268/returning-file-not-found-error
def main():
    FileRead()

def ReadFile(filename):
    files = open(filename)
    lines = files.readlines()

    for index, line in enumerate(lines):
        print(index, "=", line)

def FileRead():
    try:
        ReadFile("files.txt")

    except IOError as e:
        print("Could not open file:", e)

if __name__ == "__main__":
    main()