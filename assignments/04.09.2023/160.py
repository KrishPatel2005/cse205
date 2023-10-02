# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=c2=0
        temp1,temp2=headA,headB
        while temp1 or temp2:
            if temp1:
                c1+=1
                temp1=temp1.next
            if temp2:
                c2+=1
                temp2=temp2.next
        c=c1-c2
        if c<0:
            while c!=0:
                headB=headB.next
                c+=1
        else:
            while c!=0:
                headA=headA.next
                c-=1
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return headA
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/ 