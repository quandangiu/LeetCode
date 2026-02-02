class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def maxGain(node):
            if not node:
                return 0
            
            left_gain = max(maxGain(node.left), 0)
            right_gain = max(maxGain(node.right), 0)
            
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)
            
            return node.val + max(left_gain, right_gain)
        
        maxGain(root)
        return self.max_sum
