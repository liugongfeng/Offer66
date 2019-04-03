class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, node):
        self.inOrder = []
        root = node
        while root.next:
            root = root.next
        self.midOrder(root)
        if self.inOrder.index(node) != len(self.inOrder) -1:
            return self.inOrder[self.inOrder.index(node) + 1]
        return None 


    def midOrder(self, root):
        if not root:   return 
        self.midOrder(root.left)
        self.inOrder.append(root)
        self.midOrder(root.right)





    def method2(self, node):        
        if node.right:
            p = node.right
            while p.left:
                p = p.left
            return p

        while node.next:
            if node.next.left == node:
                return node.next
            node = node.next
        return