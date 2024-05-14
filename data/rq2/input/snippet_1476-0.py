def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C, 3))