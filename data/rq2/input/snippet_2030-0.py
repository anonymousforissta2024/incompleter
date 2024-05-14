import pandas as pd
rankings_pd = pd.DataFrame(rankings)
print(rankings_pd)
rankings_pd.rename(columns={'test': 'TEST'}, inplace=True)
print('\nAfter modifying first column:\n', rankings_pd.columns)