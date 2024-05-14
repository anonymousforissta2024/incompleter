#Source: https://stackoverflow.com/questions/54145421/typeerror-cant-concat-str-to-bytes
def create_set(feature, value):
  return b'{"type":"set","feature":'+feature+',"value":'+value+'}'

on = create_set("main.power", "on")