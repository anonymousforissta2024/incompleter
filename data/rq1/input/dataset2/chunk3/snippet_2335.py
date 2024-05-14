#Source: https://stackoverflow.com/questions/64220944/importing-open-data-set-giving-attribute-error
import opendatasets as od

dataset_url='https://www.kaggle.com/rohanrao/air-quality-data-in-india'
od.download('https://www.kaggle.com/rohanrao/air-quality-data-in-india')
data_dir = './air-quality-data-in-india'  