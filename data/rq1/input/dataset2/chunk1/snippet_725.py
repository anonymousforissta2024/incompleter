#Source: https://stackoverflow.com/questions/59577129/python3-concatenate-str-not-bytes-to-bytes-typeerror
my_dictonary = {
         "subfolder\a_file.bin" :  ["A3", "B3", "2400"] ,
         "subfolder\b_file.bin" :  ["A4", "B4", "3000"] , 
}

for d in my_dictonary :
    with open(d, "rb") as r: data = r.read()

    content= ""

    for line in my_dictonary[d]:
        content= content+ str(line) + "\n"

    file_set = set()

    for filename in glob.iglob('./**/*', recursive=True):
         file_set.add(os.path.abspath(filename))

    f_slice = d.split('\\')
    f_slice = f_slice[1].split(".bin")
    file_n = ""
    for e in file_set:
        if f_slice[0] in e and ".cap" in e:
            file_n = e

with open(file_n, 'wb') as f: f.write(content + data)