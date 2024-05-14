#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
train_set = [
    [
        x['text'],
        [{'start': y["start"], 'end': y["end"], 'tag': y["label"], 'text': y["ngram"]} for y in x['spans']]
    ] for x in train_data
]