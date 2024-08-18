class Solution:
    def isUgly(self, n: int) -> bool:
        factor=[2,3,5]

        for i in  factor:
            while n>1 and n%i==0:
                n=n//i
            if n==1:
                return True
        return False
