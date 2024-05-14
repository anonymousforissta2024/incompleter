#Source: https://stackoverflow.com/questions/64241141/how-to-solve-typeerror-sequence-item-0-expected-str-instance-float-found
docs_df = pd.DataFrame(data, columns=["Doc"])
docs_df['Topic'] = cluster.labels_
docs_df['Doc_ID'] = range(len(docs_df))
docs_per_topic = docs_df.groupby(['Topic'], as_index = False).agg({'Doc': ' '.join})