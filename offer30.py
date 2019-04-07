class Solution:
    def FindGreatestSumOfSubArray(self, arr):
        local_max = global_max = arr[0]
        for a in arr[1:]:
            local_max = max(a, local_max + a)
            global_max = max(global_max, local_max)

        return global_max