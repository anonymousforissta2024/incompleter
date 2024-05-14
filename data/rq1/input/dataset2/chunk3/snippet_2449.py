#Source: https://stackoverflow.com/questions/72999836/micropython-application-throws-attributeerror-for-very-basic-use-of-re-split-wit
s2 = re.split(r"[^a-zA-Z0-9_]+", s1)

s2 = re.split(r"[\W]+", s1)