#Source: https://stackoverflow.com/questions/58817559/iterating-on-dictionary-throws-typeerror-list-indices-must-be-integers-or-slice
num_detections = int(detection['num_detections'])
output_dict = {key:value[0, :num_detections].numpy() 
                for key,value in detection.items()}