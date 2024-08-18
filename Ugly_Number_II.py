class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=set()
        arr.add(1)
        cur=0
        for i in range(n):
            cur=min(arr)
            arr.remove(cur)
            arr.add(cur*2)
            arr.add(cur*3)
            arr.add(cur*5)
        return cur
