# 17. Letter Combinations of a Phone Number (Medium)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return
            
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))   # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations(""))     # Output: []
    print(sol.letterCombinations("2"))    # Output: ["a","b","c"]
