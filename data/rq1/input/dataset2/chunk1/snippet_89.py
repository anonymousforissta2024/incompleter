#Source: https://stackoverflow.com/questions/60750349/python-typeerror-descriptor-append-for-list-objects-doesnt-apply-to-a-int
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        c = []
        self.combSum2(0,sorted(candidates),target,result,c)
        print("result:")
        print(result)
        return result

    def combSum2(self, i: int, l: List[int], t: int, res: [], curr: []):
        if t == 0:
            print(curr)
            res.append(curr)
            return
        if t < 0:
            return
        for idx in range(i,len(l)):
            if(idx == i or l[idx] != l[idx-1]):
                curr.append(l[idx])
                self.combSum2(idx+1,l,t-l[idx],res,curr)
                del curr[-1]