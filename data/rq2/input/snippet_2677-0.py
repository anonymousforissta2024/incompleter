def gray_to_binary(n):
    """Convert Gray codeword to binary and return it."""
    n = int(n, 2)
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]
b = gray_to_binary(g)
print('In binary:', b)