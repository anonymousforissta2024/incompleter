#Source: https://stackoverflow.com/questions/59509507/formating-issue-with-list-of-integers-typeerror-not-all-arguments-converted-du
def sort_array(source_array):
    result = source_array[:]
    odd = []
    for i in result :
        if i % 2 == 0 or i == 0:
            odd.append('even_number')
        else:
            odd.append(i)
            result[i] = 'odd'

     # this is not a complete implementation we need to sort odd then replace it 
     # string 'even_number' kind off merge
    return source_array
#checking the out put below
print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])