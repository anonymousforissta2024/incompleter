def extract_path(test_dict, path_way):
    if not test_dict:
        return [path_way]
    temp = []
    for key in test_dict:
        temp.extend(extract_path(test_dict[key], path_way + [key]))
    return temp

def hlper_fnc(test_dict):
    all_paths = extract_path(test_dict, [])
    res = {}
    for path in all_paths:
        front = res
        for ele in path[::-1]:
            if ele not in front:
                front[ele] = {}
            front = front[ele]
    return res
test_dict = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}
print('The original dictionary is : ' + str(test_dict))
print('The inverted dictionary : ' + str(res))