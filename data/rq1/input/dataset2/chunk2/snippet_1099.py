#Source: https://stackoverflow.com/questions/75815295/type-error-in-matplotlib-renderer-when-saving-pcolormesh-figure
im = ax.pcolormesh(X,Y,np.transpose(data),shading='gouraud',*args,**kwargs)