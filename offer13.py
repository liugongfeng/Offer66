class Solution:
    def reOrderArray(self, arr):
        flag = -1
        for i, v in enumerate(arr):
            if v % 2:
                flag += 1
                arr.insert(flag, arr.pop(i))
        return arr