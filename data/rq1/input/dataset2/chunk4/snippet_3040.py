#Source: https://stackoverflow.com/questions/76649673/college-football-analysis-typeerror-when-obtaining-star-player-counts
# concat operation to join the dfs
teams_join_recruits = pd.concat([df_teams2013_2020, df_cfb_recruits], ignore_index=True)

# Using just the recruits dataset (@Max888) 
# pivot_table() get the Star counts    
# four arrays with four elements each - I will need to adopt this to my data -  2500+ rows
    
# importing pandas    
import pandas as pd
    
#create the dataframe    
players = pd.DataFrame({
'year': [2010,
         2010,
         2010,
         2010,
         ...],       
        'stars': ['5',
         '5',
         '5',
         '5',
         ...], 
        'team': ['Florida State',
         'Florida State',
         'Miami',
         'Miami',
         ...],
        'player': ['Dorial Green-Beckham',
         'Johnathan Gray',
         'Stefon Diggs',
         'Jameis Winston',
          ...]})