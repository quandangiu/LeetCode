# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# Helper functions for testing

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
if __name__ == "__main__":
    s = Solution()
    l1 = list_to_linkedlist([2,4,3])
    l2 = list_to_linkedlist([5,6,4])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # [7,0,8]

    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # [0]

    l1 = list_to_linkedlist([9,9,9,9,9,9,9])
    l2 = list_to_linkedlist([9,9,9,9])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # [8,9,9,9,0,0,0,1]
