#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

#Answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode()
      tail = dummy

      while l1 and l2:
        #if list1 and list2 are both not empty
        if l1.val < l2.val:
          tail.next = l1
          l1= l1.next
        else:
          tail.next = l2
          l2 = l2.next

        tail = tail.next
        # tail is updated regardless which one is larger and then keeps on the loop

      if l1:
        tail.next = l1
      elif l2:
        tail.next = l2

        #above condition is for if either of them is null

      return dummy.next


        
        