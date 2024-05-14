#Source: https://stackoverflow.com/questions/72392145/matplotlib-typeerror-plotaccessor-pie-takes-1-positional-argument-but-2-were
pop_by_region.plot.pie("Population",
                      figsize = (8, 8),
                      legends = False,
                      cmap = "Set3")

plt.show()