class Solution:
    def isValidBST(self, root):
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return validate(node.left, low, node.val) and \
                   validate(node.right, node.val, high)
        
        return validate(root)
