class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, first, mid):
        if not first or not mid:
            return None
            
        index = mid.index(first[0])
        left = mid[:index]
        right = mid[index+1:]
        root = TreeNode(first[0])
        root.left = self.reConstructBinaryTree(first[1:1+len(left)], left)
        root.right = self.reConstructBinaryTree(first[-len(right):], right)
        return root

        
        