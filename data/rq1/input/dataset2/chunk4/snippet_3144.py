#Source: https://stackoverflow.com/questions/73171934/attribute-error-when-closing-from-file-learn-python-the-hard-way-ex17
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#I am attempting to shorten the code here
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# This line is drawing the attribute error
from_file.close()