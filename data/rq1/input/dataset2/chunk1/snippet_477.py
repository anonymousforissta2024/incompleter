#Source: https://stackoverflow.com/questions/32889157/typeerror-endswith-first-arg-must-be-str-or-a-tuple-of-str-not-bool
s = 'like go goes likes liked liked liking likes like'
lst = s.split()
suffixes = ['s', 'es', 'ies', 'ed', 'ing']

counter = 0
prompt = 'like'
for x in lst:
    if x.startswith(prompt) and x.endswith(any(suffix for suffix in suffixes)):
         counter += 1