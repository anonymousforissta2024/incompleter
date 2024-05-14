#Source: https://stackoverflow.com/questions/59486590/getting-a-type-error-in-google-colab-that-was-running-just-fine
temp_arr = -np.sort(-erray,axis=1)
ent_sum = np.zeros(erray.shape[0])
loc = np.zeros(erray.shape[0])
#print(erray[-2])
#print(temp_arr)
i = 0
for row in temp_arr:
  ent_sum[i] = sum(row)
  i += 1
  for col in row:
    if i == 1:
      print(col)