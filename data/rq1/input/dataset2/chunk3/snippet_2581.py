#Source: https://stackoverflow.com/questions/49933670/extracting-field-typeerror-string-indices-must-be-integers
def validate_file(f):
    #print('File Header Validation:')

    fname=open(f)
    count=0
    for line in fname:
        if 'length' in line:
            print(line['length'])


validate_file("test1.log")