#Source: https://stackoverflow.com/questions/31687808/csv-reader-typeerror-unsupported-operand-types-for-nonetype-and-str
def csv_dict_reader(file_obj, x_obj, n_obj):

    data_in_list = []
    x=0

    reader = csv.DictReader(file_obj, delimiter=',')
    f = csv.writer(x_obj, delimiter=',', quotechar='"')
    f1= csv.writer(x_obj, delimiter=',', quotechar='"')
    f2= csv.writer(n_obj, delimiter=',', quotechar='"')

    f1.writerow(["name","email","external_id","details","notes","phone","role","restriction","organization","tags"])
    f2.writerow(["name","email","phone","office","department", "role"])

    for row in reader:
        data_in_list.append(row)

        name = data_in_list[x]['firstname'] + " " + data_in_list[x]['surname']
        firm = data_in_list[x]['firm']
        phone = data_in_list[x]['phone']
        email = data_in_list[x]['email']
        office = data_in_list[x]['office']
        department = data_in_list[x]['dept']
        details = ","
        notes = ","
        role = data_in_list[x]['role']
        restrictions = ","
        tags = ","

        f.writerow([name] + [email] + [details] + [phone] + [role] + 
               [restrictions] + [firm] + [tags] + [office] + [department])
        f2.writerow([name] + [email] + [phone] + [office] + [department] + [role])

        x= x+1
    return data_in_list

if __name__ == "__main__":

    with open("stafflist11.csv") as f_obj:
        with open("new.csv", "w") as x_obj:
            with open("user_databse_nepo.csv", "w") as n_obj:   
                csv_dict_reader(f_obj, x_obj, n_obj)