#Source: https://stackoverflow.com/questions/57426599/mpld3-error-attributeerror-list-object-has-no-attribute-canvas
plt.subplots(1, 1, figsize=(8, 2))
ecg = X
fig=plt.figure()
alt = np.arange(len(ecg))/125
fig= plt.plot(alt,ecg)
mpld3.save_html(fig,"test.html")
mpld3.fig_to_html(fig,template_type="simple")
mpld3.disable_notebook()
mpld3.show()