#Source: https://stackoverflow.com/questions/57761583/how-to-avoid-a-filenotfounderror-with-os-listdir
#loop
for filename in os.listdir(root_dir):
    if filename.endswith('.csv'):

        # Pull in the file
        df = pd.read_csv(filename)