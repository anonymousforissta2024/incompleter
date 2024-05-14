#Source: https://stackoverflow.com/questions/71867649/typeerror-a-bytes-like-object-is-required-not-str-caused-by-split-function
info = conn.execute_command("Info")
lines = info.split('\n')