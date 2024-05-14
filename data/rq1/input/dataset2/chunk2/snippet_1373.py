#Source: https://stackoverflow.com/questions/60716018/filenotfounderror-when-trying-to-rename-all-the-files-in-a-directory
import os


def main():
    x = 0
    file_ext = ".jpg"

    for filename in os.listdir("images/jaguar"):
        os.rename(filename, "Jaguar_" + str(x) + file_ext)
        x += 1


if __name__ == '__main__':
    main()