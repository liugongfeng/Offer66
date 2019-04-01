class ListNode:
    def __init(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, phead):
        cur, prev = phead, None

        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        return prev