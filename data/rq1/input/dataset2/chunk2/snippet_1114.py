#Source: https://stackoverflow.com/questions/66633121/how-do-i-create-a-new-dataframe-column-based-on-certain-conditons-as-it-gives-me
dataframe['ON/OFF'] = np.where((dataframe['Height'] == median_height) & (
                dataframe['State Hash'] == most_common_state_hash) & (dataframe['File Name']!= name_of_file), 1, 0, -1)