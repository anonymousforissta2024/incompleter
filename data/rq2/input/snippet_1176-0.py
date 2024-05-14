def test(obj, fn):
    return dict(((k, fn(v)) for k, v in obj.items()))
print('\nOriginal dictionary elements:')
print(users)
print('\nDictionary with the same keys:')
print(test(users, lambda u: u['age']))