#Source: https://stackoverflow.com/questions/57757630/typeerror-a-bytes-like-object-is-required-not-str-for-geniatagger
tagger = GeniaTagger('./geniatagger/geniatagger')
# option1: my_bytes = "This is a pen.".encode()
# option2: my_bytes = b"This is a pen."
# option3: my_bytes = bytes("This is a pen.")
my_bytes = "This is a pen.".encode('utf8')
print(type(my_bytes))
x = tagger.parse(my_bytes)