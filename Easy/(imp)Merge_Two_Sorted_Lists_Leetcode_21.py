# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        #here while will go on till l1 and l2 are empty/reach till the end of the list

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next
            #here the list will keep adding values until either of the list is empty
            tail = tail.next

        #here if l2 is empty then l1 will be added 
        if l1:
            tail.next = l1
        #we can't use else as this condition further continues to go for else where there is no defined condition and gives null result
        elif l2:
            tail.next = l2

        #if we just return dummy then it will add 0 in the beggining
        return dummy.next
