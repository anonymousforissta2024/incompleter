#Source: https://stackoverflow.com/questions/51814886/del-tuple-keys-from-nested-dict-avoid-runtime-and-type-error
for key, value in d_nans.items():
    seq_id = key
    feature_type = value
    for key, value in feature_type.items():
        for sub_key in list(feature_type.keys()):
            if sub_key[0] == 'nan':
                del dict[sub_key]