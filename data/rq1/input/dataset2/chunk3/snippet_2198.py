#Source: https://stackoverflow.com/questions/53865361/getting-type-errornonetype-is-not-iterable-in-spacy-to-build-custom-ner-model
import json
import logging
import spacy
import random
from spacy.util import minibatch, compounding
trainingfilename="C:/Users/codemen/Desktop/Timeseries Analytics/Canadianinfo.json"

logging.basicConfig(level=logging.INFO)




def ConvertDataturkToSpacy(trainingfilename):

    try:
        trainingData=[]
        lines=[]
        # reading file  and  formating  part
        with open(trainingfilename,'r') as f:
            lines=f.readlines()
        for line in lines:
            data=json.loads(line)
            text=data['content']
            entities=[]
            print('entties',entities)
            for annotation in data['annotation']:
                #print("Here is the thing")
                point=annotation['points'][0] #single point annotation part
                #print(point)
                labels=annotation['label']
                print("isintance",labels)
                if not isinstance(labels,list):#handling both list of labels or single label
                    labels=[labels]
                    print(labels)

                for label in labels:
                    #dataturks indices are inclusive but spacy indices are not so dealing with it by adding  with +1
                    #print("Test here")
                    entities.append((point['start'],point['end']+1,label))

            trainingData.append((text,{"entities":entities}))
        return trainingData
    except Exception as e:
        logging.exception("Unable to process item" + trainingfilename +"\n"+ "errror ="+str(e))
        return None

TrainingData=ConvertDataturkToSpacy(trainingfilename)