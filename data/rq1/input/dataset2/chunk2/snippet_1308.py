#Source: https://stackoverflow.com/questions/55859259/getting-attributeerror-nonetype-object-has-no-attribute-loc
top_C2_index = sum(sub_sector_df1.loc['C2']['Contribution%'].cumsum(axis=0) < 80)+1