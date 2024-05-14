#Source: https://stackoverflow.com/questions/56118004/word-frequency-analysis-typeerror-not-supported-between-instances-of-li
article_to_freq = {article:freq for article, freq in 
                   article_to_freq.items() if freq >= 3}