class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, root):
        if not root:    return []

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
            result.append(res)
            stack = nextstack

        last = []
        for i, v in enumerate(result):
            if i % 2 == 0:
                last.append(v)
            else:
                last.append(v[::-1])
        return last