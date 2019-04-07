class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        d = {}
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = d.get(e, 0) + 1
            else:
                d[v] += 1
            if d[v] > len(nums) // 2:
                return v
        return 0