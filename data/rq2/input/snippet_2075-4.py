import re
import itertools
test_str = 'gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb'
print('The original string is : ' + test_str)
print('The original list is : ' + str(test_list))
seqs = re.findall(str.join('|', test_list), test_str)
grps = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]
res = max(grps, key=lambda ele: ele[1])
print('Maximum frequency substring : ' + str(res[0]))