#Source: https://stackoverflow.com/questions/62054884/using-a-lambda-function-for-pandas-dataframe-boolean-indexing-reports-typeerror
import pandas as pd

sowpods = pd.read_csv('sowpods.csv', names=['Word'])

possible_combination = 'RE'
possible_words = pd.DataFrame([], columns=['Word'])

comb_in_word = lambda _: True if (possible_combination in _) else False # ------ line 8

sowpods_bool = sowpods['Word'].apply(comb_in_word) # --------------------------- line 10
possible_words.append(sowpods.loc[sowpods_bool, 'Word'])