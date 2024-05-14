#Source: https://stackoverflow.com/questions/58019067/filenotfounderror-when-using-os-rename-but-not-when-calling-up-print-function
import os, csv

os.chdir("/Users/.../test11")
root = "/Users/.../test11"

for file in os.listdir(): #delete ds_store files b/c they mess up index value
    if file.endswith(".DS_Store"):
        path = os.path.join(root, file)
        os.remove(path)

src = "/Users/.../test11/temp_name" # rename (date/name/index)
csvFilePath = "/Users/.../test11/temp_name/data.csv"
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        timestamp = csvRow["Timestamp"]
        name = csvRow["First name"]
        for index, folder in enumerate(os.listdir(root), start=1):
            new_folder_name = f"{timestamp}_{name}_{index}"
os.rename(src, new_folder_name)