class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=[0]
        for i in range(len(s)):
            if s[i]=='(':
                ans.append(0)
            else:
                a=ans.pop()
                ans[-1]+=max(2*a,1)
        return ans.pop()
