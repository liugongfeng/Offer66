class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        
        root = sequence[-1]            
        i = 0
        for i, v in enumerate(sequence):
            if v > root:
                break
        
        for node in sequence[i:-1]:
            if node < root:
                return False     
        
        left, right = True, True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])
         
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        
        return left and right