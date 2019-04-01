class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, head):
        processed = set()
        cur = head
        while cur:
            if cur in processed:
                return cur
            else:
                processed.add(cur)
        cur = cur.next

        return None

