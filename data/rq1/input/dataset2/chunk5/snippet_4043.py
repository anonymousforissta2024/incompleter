#Source: https://stackoverflow.com/questions/41284027/python3-csv-typeerror-valueerror-csv-error
filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames = ["id", "name", "email", "amount", "sent"]
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    #writer.writeheader()


for row in reader:
    print(row)
    writer.writerow({
            "id": row["id"],
            "name": row["name"],
            "email": row["email"],
            "amount": "1293.23",
            "sent": ""
        })