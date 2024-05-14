#Source: https://stackoverflow.com/questions/57761583/how-to-avoid-a-filenotfounderror-with-os-listdir
# Specify folder name
serial = '015'

# Specify directory (note - '...' substitute for the full path used back to the drive letter)

root_dir = '...\\CleanTemps\\{}\\'.format(str(serial)) 

#loop
for filename in os.listdir(root_dir):
    if filename.endswith('.csv'):

        print(filename)

        # Pull in the file
        df = pd.read_csv(filename)