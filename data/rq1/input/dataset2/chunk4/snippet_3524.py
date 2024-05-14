#Source: https://stackoverflow.com/questions/72649359/numpy-related-attribute-error-in-using-seaborns-pairplot
import seaborn as sns
penguins = sns.load_dataset("penguins")
sns.pairplot(penguins)