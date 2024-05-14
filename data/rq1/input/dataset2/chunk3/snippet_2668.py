#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
tree.plot_tree(clf,
               feature_names = X.columns, 
               class_names= df['Customer'],
               rounded=True, 
               filled = True,
               fontsize=7
               );