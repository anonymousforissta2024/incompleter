#Source: https://stackoverflow.com/questions/60081988/python-count-type-error-when-passing-char-casted-number
randomString = 'a-sasdqwe3123d234wdd213dsad12da-sd-sa'
for number in range(256):
    print(randomString.encode('utf-8').count(chr(number)))