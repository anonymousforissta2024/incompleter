#Source: https://stackoverflow.com/questions/49358558/typeerror-cannot-compare-type-timestamp-with-type-str-occurred-at-inde
def f(r):
    if r['balance_dt'] <= '2016-11-30':
        return 0
    else:
        return 1
df_obctohdfc['balance_dt_flag'] = df_obctohdfc.apply(f,axis=1)