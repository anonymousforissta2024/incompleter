#Source: https://stackoverflow.com/questions/59238837/typeerror-tensors-in-list-passed-to-values-of-pack-op-have-types-string-f
packed_dataset = temp_dataset.map(pack)

for features, labels in packed_dataset.take(1):
  print(features.numpy())
  print()
  print(labels.numpy())