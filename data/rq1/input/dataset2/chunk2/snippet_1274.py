#Source: https://stackoverflow.com/questions/55557384/returning-list-append-throws-typeerror-unsupported-operand-types-in-recur
def helper(cur_seq, seq, cur_i, result):
    if len(seq) == cur_i:
        return result.append(cur_seq)
    else:
        next_i = cur_i + 1
        if len(cur_seq) == 0 or seq[cur_i] > cur_seq[-1]:
            temp = cur_seq.copy()
            temp1 = cur_seq.copy()
            temp.append(seq[cur_i])
            return helper(temp, seq, next_i, result) + helper(temp1, seq, next_i, result)
        else:
            return helper(cur_seq.copy(), seq, next_i, result)


def longest_sub_sequence(seq):
    cur_seq = []

    result = helper(cur_seq, seq, 0, [])

    max_length = 0
    for i in result:
        if len(i) > max_length:
            max_length = len(i)


    return max_length


if __name__ == "__main__":

    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    y = longest_sub_sequence(seq)
    print(y)