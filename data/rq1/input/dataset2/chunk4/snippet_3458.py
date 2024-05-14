#Source: https://stackoverflow.com/questions/67772067/getting-typeerror-no-loop-matching-the-specified-signature-and-casting-was-foun
# Plotting the KDE Plot 
sns.kdeplot(x.loc[(x['gender']==1),'pixel_per_image'], color='r', shade=True, Label='Male') 
  
sns.kdeplot(x.loc[(x['gender']==0),'pixel_per_image'], color='b', shade=True, Label='Female') 
  
plt.xlabel('Avg pixel value per image') 
plt.ylabel('Probability Density') 
plt.title('Kernel Density Estimate plot to visualize probability density at different values in a continuous variable\n')
plt.show()