#Source: https://stackoverflow.com/questions/33661893/typeerror-unhashable-type-dict-dictionaries-within-lists
first_dict = {}
new_list_of_dict = [{"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"}]
for i in new_list_of_dict:
    print(i["name"])
    first_dict[i] = i["name"]
    print(first_dict)