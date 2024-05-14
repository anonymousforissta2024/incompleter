#Source: https://stackoverflow.com/questions/72392145/matplotlib-typeerror-plotaccessor-pie-takes-1-positional-argument-but-2-were
import pandas as pd
import matplotlib.pyplot as plt

required_cols =["Country",
               "Region",
               "Population",
               "Coastline (coast/area ratio)",
               "GDP ($ per capita)",
               "Literacy (%)",
               "Birthrate"]

countries = pd.read_csv("datasets/countries_of_the_world.csv",
                       usecols = required_cols,
                       decimal = ",")

countries.rename(columns = {"GDP ($ per capita)": "PerCapitaGDP",
                           "Coastline (coast/area ratio)" : "CoastLineAreaRatio",
                           "Literacy (%)" : "LiteracyRate"},
                 inplace = True)

countries = countries.dropna()

countries.head()

countries.Region.unique()

avg_by_region = countries.groupby(by = "Region").mean()

avg_by_region

avg_by_region.Birthrate.plot(kind = "bar")

plt.show()

avg_by_region.Birthrate.plot(kind = "barh",
                            title = "Avg. Birthrate by Region")
plt.show()

pop_by_region = countries[["Region", "Population"]].groupby(by = "Region").sum()



pop_by_region.plot.pie("Population",
                      figsize = (8, 8))
plt.show()

pop_by_region.plot.pie("Population",
                      figsize = (8, 8),
                      legends = False,
                      cmap = "Set3")

plt.show()