#Source: https://stackoverflow.com/questions/50351524/typeerror-nonetype-object-is-not-subscriptable-when-creating-a-pd-dataframe-d
for x in range (1, num_match + 1):
            d["Match{0}".format(x)] = [y[0] for y in aggregated_matches["Match" + str(x)]]