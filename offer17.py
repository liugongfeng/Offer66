class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, root1, root2):
        # 把root1 root2分别前序遍历，获得遍历的字符串 判断root2字符串是否在root1字符串中即可
        def helper(p):
            if p:
                return str(p.val) + helper(p.left) + helper(p.right)
            else:
                return ""

        return helper(root2) in helper(root1) if root2 else False
