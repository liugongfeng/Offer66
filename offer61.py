class TreeNode:
    def __init__(self):
        self.index = -1

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def Serialize(self, root):
        if not root:
            return "#,"
        return str(root.val) + ',' + self.Serialize(root.left) + \
                                     self.Serialize(root.right)


    def Deserialize(self, s):
        self.index += 1
        lst = s.split(',')
        if self.index >= len(s):
            return None
        root = None

        if lst[self.index] != "#":
            root = TreeNode(int(lst[self.index]))
            root.left, root.right = self.Deserialize(s), self.Deserialize(s)
        return root
        
        

one = TreeNode(1)
one.left, one.right = TreeNode(2), TreeNode(3)
one.left.left, one.left.right = TreeNode(4), TreeNode(5)
s = Solution()
res = s.Serialize(one)
print(res)


