#Source: https://stackoverflow.com/questions/57766165/attributeerror-nonetype-object-has-no-attribute-split-when-trying-to-split
df_no_dup.head()



start = datetime.now()
df_no_dup["tag_count"] = df_no_dup["Tags"].apply(lambda text: len(text.split(" ")))

print("Time taken to run this cell :", datetime.now() - start)
df_no_dup.head()