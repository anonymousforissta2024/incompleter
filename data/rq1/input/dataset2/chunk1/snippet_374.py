#Source: https://stackoverflow.com/questions/17092520/typeerror-list-does-not-support-the-buffer-interface-when-writing-bytes-to
file = open(filename + ".bmp", "rb")
data = file.read()
file.close()
new = []

for byte in data:
    byte = int(byte)
    if byte%2:#make even numbers odd
        byte -= 1
    new.append(bin(byte))

file = open(filename + ".bmp", "wb")
file.write(new)
file.close()