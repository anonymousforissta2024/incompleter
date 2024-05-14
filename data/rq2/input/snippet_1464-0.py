def decode(alist):

    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]
print('Original encoded list:')
print(n_list)
print('\nDecode a run-length encoded said list:')
print(decode(n_list))