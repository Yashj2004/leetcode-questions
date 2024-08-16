class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m=0
        min_v=arrays[0][0]
        max_v=arrays[0][-1]
        for i in range(1, len(arrays)):
            cur_m=arrays[i][0]
            cur_max=arrays[i][-1]
            m=max(m, abs(cur_max - min_v) , abs(max_v-cur_m))
            min_v=min(min_v , cur_m)
            max_v=max(max_v , cur_max)
        return m
