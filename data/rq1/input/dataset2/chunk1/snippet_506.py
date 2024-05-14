#Source: https://stackoverflow.com/questions/55895254/getting-filenotfounderror-when-trying-to-open-a-file-for-reading-in-python-3
working_dir = "data/"

for file in os.listdir(working_dir):
    if (file.find("mda") != -1):
        SIC = re.findall("__(\d+)", file)
        f = open(file, 'r')