class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, root):
        def get_Height(root):
            if not root:
                return 0
            left, right = get_Height(root.left), get_Height(root.right)

            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return get_Height(root) >= 0