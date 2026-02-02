# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Min-heap approach
        heap = []
        
        # Add first node of each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
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
    
    lists = [
        createList([1, 4, 5]),
        createList([1, 3, 4]),
        createList([2, 6])
    ]
    result = sol.mergeKLists(lists)
    print(listToArray(result))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
