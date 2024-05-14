#Source: https://stackoverflow.com/questions/69342771/attributeerror-nonetype-object-has-no-attribute-asfreq
a_df = get_dataframe_from_csv("DAX")
a_df = a_df.asfreq('d')
a_df.index