class Solution:
    def simplifyPath(self, path):
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part == '..' and stack:
                stack.pop()
            elif part and part != '.' and part != '..':
                stack.append(part)
        
        return '/' + '/'.join(stack)
