#Source: https://stackoverflow.com/questions/47954452/helping-out-with-type-error
def write_password(): 
    points = 0 
    #askpassword = input("enter in a password. only use the chasricters")
    #char = "qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM"
    askpassword = "asdf"
    char = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
    triples = []
    for chars in char:
        for i in range(len(chars)-2):
            triples.append(char[i:i+3])
    askpassword = "askpassword".strip().lower()
    for triple in triples:
        if triple in askpassword:
            points += -5
    for char in askpassword:
        if char in askpassword:
            if len (askpassword) >= 8:
                points = points + 1
            else:
                print("no points")
    print("this password is worth",points,"points")

write_password()