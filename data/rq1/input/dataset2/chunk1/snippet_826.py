#Source: https://stackoverflow.com/questions/75939176/default-collate-typeerror-batch-must-contain-tensors-numbers-dicts-or-lists
for data in dataloader:
    image, slide, filename = data['image'], data['slide_id'], data['filename']
    # predict