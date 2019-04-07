class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, root):
        if not root:
            return
        self.arr = []
        self.midTraversal(root)
        for i, v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]

    def midTraversal(self, root):
        if not root:  return 
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)