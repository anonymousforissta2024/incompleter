#Source: https://stackoverflow.com/questions/51814886/del-tuple-keys-from-nested-dict-avoid-runtime-and-type-error
for key, value in d_nans.items():
    seq_id = key
    feature_type = value
    for key, value in feature_type.items():
        if type(key) == tuple:
            if key[0] == 'nan':
                del feature_type[key]