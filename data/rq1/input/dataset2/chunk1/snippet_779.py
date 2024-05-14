#Source: https://stackoverflow.com/questions/49795022/nested-defaultdict-typeerror-first-argument-must-be-callable-or-none
dd = defaultdict(lambda: defaultdict(lambda: defaultdict([])))

dd['something1']['something11']['something111'].append('something')