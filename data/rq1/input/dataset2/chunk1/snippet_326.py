#Source: https://stackoverflow.com/questions/19285014/python-name-error-name-not-defined
def main():
    D = {} #create empty dictionary
    for x in open('wvtc_data.txt'):
        key, name, email, record = x.strip().split(':')
        key = int(key) #convert key from string to integer
        D[key] = {} #initialize key value with empty dictionary
        D[key]['name'] = name
        D[key]['email'] = email
        D[key]['record'] = record

print(D[106]['name'])
print(D[110]['email'])
main()