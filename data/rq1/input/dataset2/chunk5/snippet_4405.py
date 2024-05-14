#Source: https://stackoverflow.com/questions/55195483/typeerror-int-object-is-not-subscriptable-python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []

        for i in range(numRows):
            pascal.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    pascal.append(1)
                else:
                    pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        return pascal