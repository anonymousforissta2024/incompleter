#Source: https://stackoverflow.com/questions/36896672/pascals-triangle-type-error
def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

def pascals_triangle(rows):
    for row in range(rows):
        answer = ""
        for column in range(row + 1):
            answer = answer + combination(row, column) + "\t"
        print(answer)

pascals_triangle(10)