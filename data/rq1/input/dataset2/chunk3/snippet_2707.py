#Source: https://stackoverflow.com/questions/65279235/attributeerror-fileinput-object-has-no-attribute-read
import fileinput
import json

with fileinput.input(files=('bot_details.json')) as f:
    my_load = json.load(f)
    TOKEN=my_load["TOKEN"]