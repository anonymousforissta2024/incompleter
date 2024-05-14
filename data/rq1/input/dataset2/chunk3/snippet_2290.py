#Source: https://stackoverflow.com/questions/66434835/attributeerror-tuple-object-has-no-attribute-convert
import os
import json
import random
import csv
from pydub import AudioSegment

file_path = '/path/to/file/.tsv '
save_json_path = '/path/where/you/want/the/jsons/saved' 

def main(args):
    data = []
    directory = file_path.rpartition('/')[0]
    percent = int(100)
    
    with open(file_path, encoding="latin-1") as f:
        lenght = sum(1 for ine in f)
        
    with open(file_path, newline='') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter='\t')
        index = 1
        if(args.convert):
            print(str(lenght) + "files found")
        for row in reader:  
            file_name = row['path']
            filename = file_name.rpartition('.')[0] + ".wav"
            text = row['sentence']
            if(args.convert):
                data.append({
                "key": directory + "/clips/" + filename,
                "text": text
                })
                print("converting file " + str(index) + "/" + str(lenght) + " to wav", end="\r")
                src = directory + "/clips/" + file_name
                dst = directory + "/clips/" + filename
                sound = AudioSegment.from_mp3(src)
                sound.export(dst, format="wav")
                index = index + 1
            else:
                data.append({
                "key": directory + "/clips/" + file_name,
                "text": text
                })
                
    random.shuffle(data)

    print("creating JSON's")
    f = open(save_json_path +"/"+ "train.json", "w")
    
    with open(save_json_path +"/"+ 'train.json','w') as f:
        d = len(data)
        i=0
        while(i<int(d-d/percent)):
            r=data[i]
            line = json.dumps(r)
            f.write(line + "\n")
            i = i+1
    
    f = open(save_json_path +"/"+ "test.json", "w")

    with open(save_json_path +"/"+ 'test.json','w') as f:
        d = len(data)
        i=int(d-d/percent)
        while(i<d):
            r=data[i]
            line = json.dumps(r)
            f.write(line + "\n")
            i = i+1
    print("Done!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    Utility script to convert commonvoice into wav and create the training and test json files. """
    )
    parser.add_argument('--convert', default=True, action='store_true',
                        help='says that the script should convert mp3 to wav')

    
    args = parser.parse_known_args()
    main(args)