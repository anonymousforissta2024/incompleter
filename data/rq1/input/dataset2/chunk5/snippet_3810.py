#Source: https://stackoverflow.com/questions/57742659/im-getting-an-error-while-adding-a-new-column-with-set-up-bins-typeerror
# set up bins
bins = [0, 585, 615, 645, 675]
group_name = ['0 - 584', '585 - 614', '615 - 644', '645 +']

# add a new column: spending range
score_by_school_spending["Spending Range"] = pd.cut(score_by_school_spending["Per Student Budget"],bins,labels=group_name)
score_by_school_spending