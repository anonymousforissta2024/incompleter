#Source: https://stackoverflow.com/questions/65049767/correlation-analysis-using-seaborn-typeerror-float-object-cannot-be-interpr
import seaborn as sb
corr = V.corr()
ax = sb.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sb.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);