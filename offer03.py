class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next

        return result
