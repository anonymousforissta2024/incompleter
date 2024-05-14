#Source: https://stackoverflow.com/questions/72340628/typeerror-object-of-type-int64-is-not-json-serializable-while-converting-to-par
df4.to_parquet('df4.parquet.gzip',compression='gzip')