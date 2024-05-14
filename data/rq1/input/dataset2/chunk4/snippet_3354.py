#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
ori_label_list = []
for line in train_set:
    ori_label_list += [entity['tag'] for entity in line[1]]

ori_label_list = sorted(list(set(ori_label_list)))

label_list = []
for prefix in 'BI':
    label_list += [prefix + '-' + x for x in ori_label_list]
label_list += ['O']
label_list = sorted(list(set(label_list)))
label2id = {n:i for i,n in enumerate(label_list)}
id2label= {i:n for i,n in enumerate(label_list)}