import itertools
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)