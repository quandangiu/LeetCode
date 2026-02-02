# 24. Swap Nodes in Pairs (Medium)
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swap nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move to next pair
            prev = first
        
        return dummy.next


# Helper function to create linked list from array
def createList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to array
def listToArray(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    head = createList([1, 2, 3, 4])
    result = sol.swapPairs(head)
    print(listToArray(result))  # Output: [2, 1, 4, 3]
    
    head = createList([])
    result = sol.swapPairs(head)
    print(listToArray(result))  # Output: []
    
    head = createList([1])
    result = sol.swapPairs(head)
    print(listToArray(result))  # Output: [1]
