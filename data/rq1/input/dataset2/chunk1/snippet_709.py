#Source: https://stackoverflow.com/questions/42602399/attributeerror-function-object-has-no-attribute-sum-pandas
death_2013['percent_of_total'] = death_2013.count.apply(
     lambda x: (x / death_2013.count.sum()))