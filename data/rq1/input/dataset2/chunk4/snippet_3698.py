#Source: https://stackoverflow.com/questions/62135331/python-typeerror-cant-pickle-module-objects-multiprocessing-on-jupyter-notebo
with open('file', 'r') as o:
    vis_reader = csv.reader(o,delimiter='|')
    vis_items = list(vis_reader)

vis_data = pd.DataFrame(vis_items) 
all_other_vis_item_desc = vis_data[1]
vis_item_size = vis_data[2]

choice_mappings = {choice: utils.default_process(choice) for choice in all_vis_item_desc}

def find_match(x):
    match_description = process.extractOne(
                                    utils.default_process(x),
                                    choice_mappings,
                                    processor=None,
                                    scorer=fuzz.token_sort_ratio,
                                    score_cutoff=65)
    #check if the size match or no
    if match_description:    
        #check if the size match 
        eby_item_size = re.sub(r'(?<=\d)Z\b', r' oz ',x)
        eby_item_size = re.sub(r'/(?=\d)', r' ct ',eby_item_size)
        eby_item_size = {x[0].replace(" ", "").lower() for x in findall(regex_size, eby_item_size)}
        vis_item_desc = match_description[0]
        vis_item_size = vis_items[all_vis_item_desc.index(vis_item_desc)]
        vis_item_size = vis_item_size[2]
        if(vis_item_size.replace(" ", "").lower() in eby_item_size):
            print("size match")
            cross_reference_values = vis_items[all_vis_item_desc.index(vis_item_desc)]
            print(x)
            print(cross_reference_values)
            message = "Decription match"
            size_match = "size match"
            ratio_matching = match_description[1]
        elif not eby_item_size:
            print("match")
            cross_reference_values = vis_items[all_vis_item_desc.index(vis_item_desc)]
            print(x)
            print(cross_reference_values)
            message = "Decription match"
            size_match = "review size match"
            ratio_matching = match_description[1]
    return match_description

import numpy as np
from multiprocessing import Pool
import find_match

num_partitions = 10 #number of partitions to split dataframe
num_cores = 4 #number of cores on your machine

def parallelize(df, func):
    print("parallelizing")
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

#read in the csv file of a list of items to pandas df
eby_data = read_eby1()

data = parallelize(eby_data, find_match)