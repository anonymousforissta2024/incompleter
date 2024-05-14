#Source: https://stackoverflow.com/questions/71173098/filenotfounderror-errno-2-no-such-file-or-directory-discrepancy-between-prog
# Datengenerierung für Logname, Kundennummer, Zeit
num_dt = datetime.now()
num_dt_l = num_dt.strftime("%d_%m_%Y %HH_%MM_%SS")
rndnr = str(random.randint(1, 9999))
log_n = r"Logs/" + str(num_dt_l) + "__" + rndnr + r".txt"


# Print-Funktion
def logp(lv1, lv2):
    with redirect_stdout(open(log_n, 'a')):
        print("-----------\n" + str(datetime.now().strftime("%HH:%MM:%SS")) + " " + str(lv1) + " " + str(lv2) + ".")


with redirect_stdout(open(log_n, 'a')):
    print("****************************\nTest", "started\n****************************")

logp("Global Number: " + str(rndnr), "")
logp("Datum ist:", num_dt_l)