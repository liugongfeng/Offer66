class Solution:
    def minNumberInRotateArray(self, arr):
        if len(arr) == 0:
            return 0
        
        for i, v in enumerate(arr):
            if v > arr[i+1]:
                return arr[i+1]
        return arr[-1]