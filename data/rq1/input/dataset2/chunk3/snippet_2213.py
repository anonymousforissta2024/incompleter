#Source: https://stackoverflow.com/questions/52389994/encrypting-text-with-cesar-cipher-str-replace-gives-typeerror-cant-convert-n
import argparse

def parse_command_line():  
    parser=argparse.ArgumentParser()
    parser.add_argument("infile",type=str,help="input file to be encrypted or decrypted")

    parser.add_argument("-o outfile_path","--outfile outfile_path",type=str,help="output file")
    parser.add_argument("-k KEY","--key KEY",type=int,default=1,help="encryption/decryption key (must be positive) (default= 1)")
    parser.add_argument("-d","--decrypt",action="store_true",help="decrypt the input file")
    parser.add_argument("-a","--all",action="store_false",help="decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost orunknown)")
    parser.add_argument("-v","--verbose",action="store_true",help="Verbose mode")

    args=parser.parse_args()
    return args 
    pass



def transform(message, key, decrypt):

    #TODO: Your code goes here
    if decrypt:
        for i in message:
            temp=shift(i,key)
            transformed_message=message.replace(i,temp,1)
            message=transformed_message
    return transformed_message
    pass
def shift(char, key):     
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]

    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]

        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char

def main():
    # parse command line arguments
    args = parse_command_line()

    # key is specified
    if not args.all:
        # encrypt/decrypt content of infile
        outstring = transform(instring, args.key, args.decrypt)

        # write content of outstring to outfile
        write_file(outstring, args.outfile)

    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in range(1, 26):
            # decrypt content of infile
            outstring = transform(instring, k, True)

            # write content of outstring to outfile
            write_file(outstring, "decrypted_by_" + str(k) + ".txt")

if __name__ == '__main__':
    main()