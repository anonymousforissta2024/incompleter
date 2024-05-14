#Source: https://stackoverflow.com/questions/54593676/how-to-fix-featurtools-type-error-on-colab
import pandas as pd

import featuretools as ft

df1 = pd.DataFrame({'df_index' : [1,2,3,4,5],
                 'location':['aust','aust','aust','canada','canada'],
                  'prices':[34,52,46,25,67],
                   'values':[786,345,123,654,841]
                  })

es = ft.EntitySet(id='Transactions')

es.entity_from_dataframe(entity_id='log', 
                         dataframe=df1, 
                         index='df_index',
                         time_index='date'
                        )

es.normalize_entity(base_entity_id='log', new_entity_id='loc', index= 'location' )


fm, features = ft.dfs(entityset=es, target_entity='log',
                      trans_primitives = ['add', 'multiply'],
                      agg_primitives = ['sum', 'mean'],
                      max_depth = 2,
                      verbose = 2
                     )