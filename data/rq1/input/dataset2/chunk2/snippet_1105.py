#Source: https://stackoverflow.com/questions/55978423/how-to-fix-typeerror-unhashable-type-list-error
updated_list = []
new_string = re.sub('\d+', [i for i in list], s,1)
updated_list.append(new_string)
print(updated_list)