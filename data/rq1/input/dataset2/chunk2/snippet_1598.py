#Source: https://stackoverflow.com/questions/49575466/typeerror-in-string-requires-string-as-left-operand-not-list-list-compreh
top_words_list = ['great', 'love', 'good',
                  'story', 'loved', 'excellent',
                  'series', 'best', 'one']
[1 if re.search(top_words_list) in i else 0 for i in amazon['reviewer_summary']]