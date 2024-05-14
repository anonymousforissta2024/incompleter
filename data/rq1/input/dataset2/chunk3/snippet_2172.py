#Source: https://stackoverflow.com/questions/58294472/typeerror-a-bytes-like-object-is-required-not-str-but-type-shows-bytes
print(type(body))
body = body.replace('\n', '<br>')