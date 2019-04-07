class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, root):
        if not root:  return []
        stack = [root]
        result = []
        while stack:
            res = []
            nextstack = []
            for i in stack:
                res.append(i.val)
                if i.left:
                    nextstack.append(i.left)
                if i.right:
                    nextstack.append(i.right)
            stack = nextstack
            result.append(res)
        return result
