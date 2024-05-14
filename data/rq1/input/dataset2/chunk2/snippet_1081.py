#Source: https://stackoverflow.com/questions/57106707/attributeerror-set-object-has-no-attribute-to-csv
result = set(data).difference(set(df_row))
result.to_csv("part1left.txt")