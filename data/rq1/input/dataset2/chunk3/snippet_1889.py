#Source: https://stackoverflow.com/questions/41949567/getting-ggplot-python-error-nameerror-name-stat-function-is-not-defined
from ggplot import *

ggplot(counts, aes(x='pred_prob',y='true_prob',size='count')) + \
    geom_point(color='blue') + \
    stat_function(fun=lambda x: x, color='red') + \
    xlim(-0.05,  1.05) + ylim(-0.05,1.05) 