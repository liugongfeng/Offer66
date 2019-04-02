class ListNode:
    def __init(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, head):
        prev = None
        cur = head
        nextnode = None

        while cur:
            if cur.next and cur.next.val == cur.val:
                nextnode = cur.next
                while nextnode.next and nextnode.next.val == cur.val:
                    nextnode = nextnode.next
                if cur == head:
                    head = nextnode.next
                else:
                    prev.next = nextnode.next
                cur = nextnode.next
            else:
                prev, cur = cur, cur.next
        return head
    
    
    def method2(self, head):
        prev = None
        cur = head
        nextNode = None
        while cur:
            if cur.next != None and cur.val == cur.next.val:
                nextNode = cur.next
                while nextNode.next != None and nextNode.next.val == cur.val:
                    nextNode = nextNode.next
            
                if cur == head:
                    head = nextNode.next
                else:
                    prev.next = nextNode.next
                cur = nextNode.next
            else:
                prev, cur = cur, cur.next

        return head

