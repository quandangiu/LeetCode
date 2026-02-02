class Solution:
    def pathSum(self, root, targetSum):
        result = []
        
        def dfs(node, target, path):
            if not node:
                return
            
            path.append(node.val)
            
            if not node.left and not node.right and node.val == target:
                result.append(path[:])
            
            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)
            
            path.pop()
        
        dfs(root, targetSum, [])
        return result
