#Source: https://stackoverflow.com/questions/58800137/rpy2-typeerror-parameter-categories-must-be-list-like
import rpy2, rpy2.robjects as robjects, rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
import os
from rpy2.robjects.packages import importr
base = importr('base')
print(base.R_home())

# install packages in r from python

packageNames  = ('ggplot2', 'hexbin', 'MVN','afex', 'emmeans')
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

packnames_to_install = [x for x in packageNames if not rpackages.isinstalled(x)]

if len(packnames_to_install) > 0:
    utils.install_packages(StrVector(packnames_to_install))


# Read table function in r to python dataframe
data = robjects.r('read.table(file =' \
       '"http://personality-project.org/r/datasets/R.appendix3.data", header = T)')

data.head()