class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        s=0
        e=len(n)-1
        while s<e:
            a=n[s]+n[e]
            if a==t:
                return [s+1,e+1]
            elif a>t:
                e-=1
            else:
                s+=1
                
