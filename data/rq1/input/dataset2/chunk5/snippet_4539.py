#Source: https://stackoverflow.com/questions/65641396/how-to-solve-the-python-error-nameerror-name-x-is-not-defined
#!/bin/python3 
def clear_line():
    print("\n")

def id_check(id,gender):
                    
    id = input(" Do you have an id? : ")    


    if (id == "yes" ) or (id == "Yes") or (id == "y"):
        
        id = True   
    
    elif (id == "no" ) or (id == "No") or (id == "n"):
        
        print ("I need your id")
                
    else:
        print ("Please respound with yes or no "), 
        clear_line()
        id_check(id)

    gender = input(" What is you gender ? ")
    print (gender)

id_check(id,gender) 