#Source: https://stackoverflow.com/questions/75011399/typeerror-string-indices-must-be-integers-in-the-chess-com-api
from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()


def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category:', category)
        # idx = index
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


print_leaderboards()