#Source: https://stackoverflow.com/questions/59698266/typeerror-cant-multiply-sequence-by-non-int-of-type-numpy-float64-multiply
list = []

i = 1
for col in df.columns[1:19]:

    #calculations
    x = df[[df.columns[i], df.columns[i+1], df.columns[i+2]]].values
    Q = np.cov(x.T)

    eval, evec = np.linalg.eig(Q)

    w = np.array([2*(evec[0,2]/evec[1,2]),2*(evec[1,2]/evec[1,2]),2*(evec[2,2]/evec[1,2])])

    #create new columns in dataframe with applied weights
    df['w1_PCA'] = df.columns[i] * w[0]
    df['b_PCA'] = df.columns[i+1] * w[1]
    df['w2_PCA'] = df.columns[i+2] * w[2]

    i = i + 1

print(x)