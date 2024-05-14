#Source: https://stackoverflow.com/questions/54598635/typeerror-unsupported-operand-types-for-int-and-list-error
class Solution:
    def maxSubArray(self,A):
        sum_2=[]

        for i in range(0,len(A)):
            for j in range(1,len(A)-1):


                sum_1 = A[i]+A[:j]
                sum_2.append(sum_1)
        print(sum_2)
        print(max(sum_2))

s=Solution
q=[-2,1,-3,4,-1,2,1,-5,4]

s.maxSubArray('w',q)