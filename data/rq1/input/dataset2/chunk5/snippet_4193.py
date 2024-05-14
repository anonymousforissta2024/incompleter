#Source: https://stackoverflow.com/questions/58505289/stackplot-typeerror-ufunc-isfinite-not-supported-for-the-input-types
diet_projection = perc_contributions_WRAP.percentage_contributions(diet_props, 2050, 1961, 2013)

print(diet_projection.iloc[:].values)
print(np.arange(2013, 2051, 1))

plt.stackplot(np.arange(2013, 2051, 1), diet_projection.iloc[:].values)
# plt.legend(loc = "upper left")
# plt.ylabel("Diet makeup - kcal/capita/day")
# plt.xlabel("Year")
# plt.xticks(np.arange(2010, 2050, 5))
plt.show()