#Source: https://stackoverflow.com/questions/58572142/typeerror-argument-of-type-windowspath-is-not-iterable
train_images = ([x for x in all_images if val_families not in x])
val_images = ([x for x in all_images if val_families in x])