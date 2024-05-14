#Source: https://stackoverflow.com/questions/65322686/why-am-i-receiving-either-a-typeerror-or-unicode-decode-error
def read_file(filename):
    '''procedure to open a file and read its contents'''
    #open a file
    file = open(filename, 'r')
    #read the file
    filetext = file.read()
    #close the file
    file.close

#read the file 'passwords.txt'
read_file('passwords.txt')

#convert file contents into a common hash
def hash_text(filename):
    ''' Function takes contents of the file passwords.txt and converts it to
        SHA1, saving result in a new file'''
    #read the passwords.txt file
    read_file('passwords.txt')
    #import hashlib
    import hashlib
    #hash whatever file is input 
    hash_object = hashlib.sha1(filename)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    #create a new file to store the hashed passwords in
    hash_store = open("hashwords.txt", "x", "a")
    #write to the file
    hashedtext = hash_store.append()
    #close the file
    hash_store.close

#run the function
hash_text('passwords.txt')