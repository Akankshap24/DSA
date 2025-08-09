class Solution:
    def combinationSum(self, C: List[int], T: int) -> List[List[int]]:
        res=[]
        def f(i,p,s):
            if s==T: res.append(p); return
            if s>T or i==len(C): return
            f(i,p+[C[i]],s+C[i]); f(i+1,p,s)
        f(0,[],0)
        return res

        