#Source: https://stackoverflow.com/questions/77441584/attributeerror-tuple-object-has-no-attribute-split-options-list-using-pick
quizzes = os.listdir()
title = '-----------\n QUIZZABLE \n-----------\n   Quiz    \n-----------'
options = [quizzes, 'Return']
option, index = pick(options, title, indicator='[>]', default_index=0)