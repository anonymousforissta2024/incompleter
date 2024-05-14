#Source: https://stackoverflow.com/questions/75909808/attributeerror-countvectorizer-object-has-no-attribute-get-feature-names
from sklearn.decomposition import LatentDirichletAllocation
vectorizer = CountVectorizer(
            analyzer='word',       
            min_df=3,# minimum required occurences of a word 
            stop_words='english',# remove stop words
            lowercase=True,# convert all words to lowercase
            token_pattern='[a-zA-Z0-9]{3,}',# num chars > 3
            max_features=5000,# max number of unique words
            )


data_matrix = vectorizer.fit_transform(df_clean['question_lemmatize_clean'])

                                                                    
lda_model = LatentDirichletAllocation(
            n_components=10, # Number of topics
            learning_method='online',
            random_state=20,       
            n_jobs = -1  # Use all available CPUs
            )
    
    
lda_output = lda_model.fit_transform(data_matrix)
                                                                    

import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
pyLDAvis.sklearn.prepare(lda_model, data_matrix, vectorizer, mds='tsne')    