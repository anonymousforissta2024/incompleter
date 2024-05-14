#Source: https://stackoverflow.com/questions/60129510/nameerror-name-players-data-is-not-defined
asia = open_exl('pubg_as.xls', 0)
eu = open_exl('pubg_eu.xls', 0)
na = open_exl('pubg_na.xls', 0)
oc = open_exl('pubg_oc.xls', 0)
sea = open_exl('pubg_sea.xls', 0)

# Load all data
all_data = np.genfromtxt('PUBG_Player_Statistics.csv', delimiter=',')
all_data[:, 28] = all_data[:, 28] * 100

# Train data
train_data = all_data[1:2000, :][:, [3, 2, 28, 9]]
test_data = all_data[2000:, :][:, [3, 2, 28, 9]]

data = np.vstack((asia[1:], eu[1:], na[1:], oc[1:], sea[1:], players_data[1:]))
df = pd.DataFrame({data[0, i]: data[1:, i] for i in range(data.shape[1])})
m = asfloat(data[1:, :4])