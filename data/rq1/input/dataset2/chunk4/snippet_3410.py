#Source: https://stackoverflow.com/questions/75439120/drop-duplicates-groupby-typeerror-sequence-item-0-expected-str-instance
### Concat LI related columns
list_LI_concat_cols = ['LI_date_engr_sign', 'Subst_SSO', 'Subst_name', 'Subst_mang_SSO',
    'Subst_mang_name', 'Signoff_name']

### Convert to string
df1.loc[:, ['Subst_SSO','Subst_mang_SSO']] \
    = df1.loc[:, ['Subst_SSO','Subst_mang_SSO']].fillna('0').astype(int).astype(str)

### Aggr data per MRB_LI
for col in list_LI_concat_cols:
    df_subst_concat = df1.drop_duplicates(subset=['MRB_LI#', col], keep='last') \
        .groupby('MRB_LI#')[col].agg(lambda x: ' | '.join(x)).reset_index()
    df_LI = df_LI.merge(df_subst_concat, how='left', on='MRB_LI#')