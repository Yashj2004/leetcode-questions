class Solution:
    def isHappy(self, n: int) -> bool:

        def sep(num):
            ans=[]
            while num>0:
                ans.append(num%10)
                num=num//10
            return (ans)

        def single(nums):
            ans=0
            for i in range(len(nums)):
                ans+=(nums[i]*nums[i])
            return (ans)

        while n>9:
            nums=sep(n)
            n=single(nums)
        if n==1 or n==7:
            return True
        else :
            return False
