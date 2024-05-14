def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2)
    n ^= n >> 1
    return bin(n)[2:]
b = binary_to_gray(g)
print('Gray codeword:', b)