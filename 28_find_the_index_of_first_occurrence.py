# 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Simple approach using Python's find
        # return haystack.find(needle)
        
        # Manual implementation
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.strStr("sadbutsad", "sad"))  # 0
    print(sol.strStr("leetcode", "leeto"))  # -1
    print(sol.strStr("hello", "ll"))  # 2
