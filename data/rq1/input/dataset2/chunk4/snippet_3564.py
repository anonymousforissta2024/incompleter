#Source: https://stackoverflow.com/questions/72598949/appending-new-value-to-dictionary-key-gives-attributeerror-int-object-has-no
movies = ['star wars', 'avenger', 'iron man', 'spider man', 'star wars', 'spider man', 'iron man', 'star wars', 'star wars']
schedule = {}

for day, movie in enumerate(movies):
  if movie not in schedule:
    schedule[movie] = day
  else:
    schedule[movie].append(day)
print(schedule)