class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=[0,0,0]
        for i in range(len(bills)):
            if bills[i]==5:
                change[0]+=1
            elif bills[i]==10 and change[0]>=1:
                change[1]+=1
                change[0]-=1
            elif bills[i]==20 and change[0]>=1 and change[1]>=1:
                change[0]-=1
                change[1]-=1
                change[2]+=1
            elif bills[i]==20 and change[0]>=3:
                change[0]-=3
                change[2]+=1
            else:
                return False
        return True

