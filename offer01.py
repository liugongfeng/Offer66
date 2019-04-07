class Solution:
    def Find(self, target, array):
        if not array:    return 
            
        for i, v in enumerate(array):
            for j, u in enumerate(array[0]):
                if array[i][j] == target:
                    return True
        return False

        