#Source: https://stackoverflow.com/questions/67732898/what-is-this-error-and-how-to-get-rid-of-it-typeerror-argument-of-type-nonety
def color_red(val):
  color= 'red' if '|' in val else 'black'
  return 'color: %s' % color
s = df.style.applymap(color_red)
st = s.render()