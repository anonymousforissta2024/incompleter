#Source: https://stackoverflow.com/questions/59159518/list-of-lists-typeerror-unhashable-type-list
lst = [['Descendant Without A Conscience', 'good', 'happy'], ['Wolf Of The Solstice', '30000', 'sad'], ['Women Of Hope', '-4000', 'neutral'], ['Pirates Of Perfection', '65467', 'neutral'], ['Warriors And Soldiers', '-5435', 'sad'], ['Butchers And Soldiers', '76542', 'sad'], ['World Of The Mountain', '6536543', 'sad'], ['Ruination Of Dusk', '-2000', 'happy'], ['Destroying The Stars', '5435', 'happy'], ['Blinded In My Enemies', '765745.5', 'happy'], ['Descendant Without A Conscience', 'good', 'happy']]

check_lst = list(set(lst))

for movie in lst:

   if len(movie) > 3:

       raise ValueError('Invalid input.')


   elif movie[2] != movie[2].lower():

       raise ValueError('Invalid input.')

   elif len(lst) != len(check_lst):
       raise ValueError('Invalid input.')