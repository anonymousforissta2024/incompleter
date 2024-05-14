#Source: https://stackoverflow.com/questions/71344431/lambda-helper-function-with-typeerror-not-supported-between-instances-of-n
def search_clinic(search, array):
    new_array = []
    exact_match = []
    partial_match = []
    no_match = []
    # finding mathces and storing them
    for clinic in array:
        if search == clinic:
            exact_match.append(clinic)
        elif search in clinic:
            partial_match.append(clinic)
        else:
            no_match.append(clinic)
    # ordering the stored values to one array 
    for clinic in exact_match:
        new_array.append(clinic)
    for clinic in partial_match:
        new_array.append(clinic)
    for clinic in no_match:
        new_array.append(clinic)
    return new_array
#O(n) linear function   
print(search_clinic('care corp', ['healthcare corp', 'healthcare group', 'care corp', "345gyht", "zelthcare corp", "zelthcare group"]))

# I was unsatisfied with the above solution and went back to attempting to use key= 
def helper(clinic, search): 
    if clinic.find(search) != -1:
        clinic.find(search)
        # use inf to push clinics without search to end of the list
        return float('inf')
def search_clinic2(search, array):
    return sorted(array, key= lambda clinic: helper(clinic, search))

print(search_clinic2('care corp', ['healthcare corp', 'healthcare group', 'care corp', "345gyht", "zelthcare corp", "zelthcare group"]))