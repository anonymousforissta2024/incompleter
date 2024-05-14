#Source: https://stackoverflow.com/questions/46760474/facing-error-typeerror-int-object-is-not-iterable-when-sum-total-count
import glob

def stats():

    commaCount = 0

    path = 'D:/Stiudies/Data/female/*.txt'
    inf = glob.glob(path)

    for name in inf:
        with open(name, 'r', encoding="utf8") as input_file:
            for line in input_file:
                for char in line:
                    if char == ',':
                        commaCount += 1

                        total = sum(commaCount)

            print(commaCount)

stats()