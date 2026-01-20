# 44. Wildcard Matching
# Difficulty: Hard
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] means s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Handle patterns starting with *
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * matches empty or one more character
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isMatch("aa", "a"))  # False
    print(sol.isMatch("aa", "*"))  # True
    print(sol.isMatch("cb", "?a"))  # False
    print(sol.isMatch("adceb", "*a*b"))  # True
