class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        
        res = None
        while stack1 and stack2:
            pop1 = stack1.pop()
            pop2 = stack2.pop()
            if pop1 is pop2:
                res = pop1
            else:
                break
        return res



    def method2(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None

        lst1, lst2 = pHead1, pHead2
        length1 , length2 = 0, 0
        while lst1:
            length1 += 1
            lst1 = lst1.next
        while lst2:
            length2 += 1
            lst2 = lst2.next

        if length1 > length2:
            for i in range(length1 - length2):
                length1 -= 1
                pHead1 = pHead1.next
        else:
            for i in range(length2 - length1):
                length2 -= 1
                pHead2 = pHead2.next
        
        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None




