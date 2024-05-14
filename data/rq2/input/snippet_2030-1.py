import pandas as pd
rankings = {'test': ['India', 'South Africa', 'England', 'New Zealand', 'Australia'], 'odi': ['England', 'India', 'New Zealand', 'South Africa', 'Pakistan'], 't20': ['Pakistan', 'India', 'Australia', 'England', 'New Zealand']}
print(rankings_pd)
rankings_pd.rename(columns={'test': 'TEST'}, inplace=True)
print('\nAfter modifying first column:\n', rankings_pd.columns)