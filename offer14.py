class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k == 0:
            return None

        first = head
        last = head
        for i in range(k - 1):
            if not first.next:
                return None
            else:
                first = first.next
        
        while first.next:
            first = first.next
            last = last.next

        return last
