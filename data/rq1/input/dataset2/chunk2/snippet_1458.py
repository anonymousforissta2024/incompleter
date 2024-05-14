#Source: https://stackoverflow.com/questions/63936009/getting-attribute-error-str-has-no-attribute-get
dictionary = {
'one':{'random':'random answer'},
'two':{'random':'another answer'}
}

for item in dictionary:
  print(item.get('random'))