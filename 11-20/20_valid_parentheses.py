# 20. Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Pop from stack if not empty, else use dummy value
                top = stack.pop() if stack else '#'
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0


# Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))        # Output: True
    print(sol.isValid("()[]{}"))    # Output: True
    print(sol.isValid("(]"))        # Output: False
    print(sol.isValid("([)]"))      # Output: False
    print(sol.isValid("{[]}"))      # Output: True
