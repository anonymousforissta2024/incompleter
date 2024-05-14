#Source: https://stackoverflow.com/questions/54998967/attributeerror-list-object-has-no-attribute-feature
def tree_to_code(tree, feature_names):
    tree_ = tree.estimators_
    #print(tree_)
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))
    symptoms_present = []
    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print(name + " ?")
            ans = input()
            ans = ans.lower()
            if ans == 'yes':
                val = 1
            else:
                val = 0
            if  val <= threshold:
                recurse(tree_.children_left[node], depth + 1)
            else:
                symptoms_present.append(name)
                recurse(tree_.children_right[node], depth + 1)
        else:
            present_disease = print_disease(tree_.value[node])
            print( "You may have " +  present_disease )
            red_cols = reduced_data.columns 
            symptoms_given = red_cols[reduced_data.loc[present_disease].values[0].nonzero()]
            print("symptoms present  " + str(list(symptoms_present)))
            print("symptoms given "  +  str(list(symptoms_given)) )  
            confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
            print("confidence level is " + str(confidence_level))

    recurse(0, 1)

tree_to_code(clf,cols)