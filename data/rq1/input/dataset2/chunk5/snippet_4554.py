#Source: https://stackoverflow.com/questions/69706223/how-to-solve-this-typeerror-in-lambda-functions
def even_odd_lambda(list_object):
  
    #odd_ctr = list(filter(lambda x: (x%2 != 0) , list_1))
    #even_ctr = list(filter(lambda x: (x%2 == 0) , list_1))
    
    odd_ctr = len(list(filter(lambda x: (x%2 != 0) , list_object)))
    even_ctr = len(list(filter(lambda x: (x%2 == 0) , list_object)))

    return [odd_ctr, even_ctr] 


if __name__ == '__main__':
  
    a=input("Add list elements seperated by space ").split(' ')

    
    
    output = even_odd_lambda(a)
    print("\nNumber of even numbers in the above array: ", output[1])
    print("\nNumber of odd numbers in the above array: ", output[0])  