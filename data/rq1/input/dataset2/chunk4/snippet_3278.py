#Source: https://stackoverflow.com/questions/75196015/typeerror-raised-even-if-the-variable-seems-to-be-of-the-right-type
txt = 'Some text, dude!'
with open('to_load', mode='wb') as f:
   raw = txt.encode('ascii')
   print(raw, file=f)