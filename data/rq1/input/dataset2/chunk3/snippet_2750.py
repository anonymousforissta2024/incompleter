#Source: https://stackoverflow.com/questions/60479597/error-attributeerror-dataframe-object-has-no-attribute-source-or-keyerr
names = [data['source'] == i for i in indices]

plt.figure()
plt.title("Feature Importance")
plt.bar(range(source.shape[1]), importances[indices])
plt.xticks(range(source.shape[1]), names, rotation=90)
plt.show()