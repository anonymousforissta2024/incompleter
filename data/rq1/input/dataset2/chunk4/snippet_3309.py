#Source: https://stackoverflow.com/questions/64833301/typeerror-precision-score-got-an-unexpected-keyword-argument-y-pred
cancer_data = datasets.load_breast_cancer()

X = cancer_data.data
Y = cancer_data.target