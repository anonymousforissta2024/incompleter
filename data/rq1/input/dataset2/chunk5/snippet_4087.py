#Source: https://stackoverflow.com/questions/58706487/attributeerror-numpy-ndarray-object-has-no-attribute-sqrt
df=pd.DataFrame({'Value':[-0.016,-0.006,0.003,-0.011,-0.036,-0.031,-0.014,-0.006,-0.01 ,-0.009,0.004,0.001,-0.012,-0.021,-0.008,0.001,-0.011,-0.01,-0.006,0.002,0.004],'Nmae':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})

x=pd.DataFrame([x.values.sqrt(np.mean(df2['Value']**2)) for x in np.array_split(df2, (len(df2)/10))])