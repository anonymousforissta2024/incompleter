#Source: https://stackoverflow.com/questions/69029301/issue-typeerror-float-object-is-not-subscriptable
df['IMDb'] = [float(rating[0:3]) for rating in df['IMDb']]