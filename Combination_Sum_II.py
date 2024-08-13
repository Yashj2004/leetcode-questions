class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans=[]

        def backtrack(candidates,target,start,path):
            if target==0:
                self.ans.append(path.copy())
                return 
            if target<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                print(path)
                backtrack(candidates,target-candidates[i],i+1,path+[candidates[i]])
        backtrack(candidates,target,0,[])
        return self.ans
