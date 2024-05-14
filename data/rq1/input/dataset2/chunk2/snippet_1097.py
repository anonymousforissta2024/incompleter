#Source: https://stackoverflow.com/questions/55312601/attribute-error-module-lightgbm-has-no-attribute-lgbmclassifier-and-datas
import lightgbm as gbm 

d_train=gbm.Dataset(train_x,label=train_y)