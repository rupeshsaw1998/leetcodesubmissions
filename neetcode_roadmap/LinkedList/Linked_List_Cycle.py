##Given head, the head of a linked list, determine if the linked list has a cycle in it.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Return true if there is a cycle in the linked list. Otherwise, return false.
#ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        #we are using two pointers both starting at head/first element of the list

        while fast and fast.next:
            #while fast and fast.next is not null this while loop will keep running
            slow = slow.next
            #slow increases by 1 
            fast = fast.next.next
            #fast increases by 2
            if slow == fast:
                #if both meet then it'll be a loop
                return True

        return False
