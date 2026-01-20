# 25. Reverse Nodes in k-Group (Hard)
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Check if there are at least k nodes
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        # Reverse k nodes starting from head
        def reverseK(head, k):
            prev = None
            current = head
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev, head, current  # new_head, tail, next_group_head
        
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        
        while hasKNodes(prev_group_tail.next, k):
            new_head, tail, next_group_head = reverseK(prev_group_tail.next, k)
            prev_group_tail.next = new_head
            tail.next = next_group_head
            prev_group_tail = tail
        
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
    
    head = createList([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 2)
    print(listToArray(result))  # Output: [2, 1, 4, 3, 5]
    
    head = createList([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 3)
    print(listToArray(result))  # Output: [3, 2, 1, 4, 5]
