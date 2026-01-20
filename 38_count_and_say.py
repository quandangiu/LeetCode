# 38. Count and Say
# Difficulty: Medium
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Get previous result
        prev = self.countAndSay(n - 1)
        
        result = []
        count = 1
        
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result.append(str(count) + prev[i - 1])
                count = 1
        
        # Don't forget the last group
        result.append(str(count) + prev[-1])
        
        return ''.join(result)


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.countAndSay(1))  # "1"
    print(sol.countAndSay(2))  # "11"
    print(sol.countAndSay(3))  # "21"
    print(sol.countAndSay(4))  # "1211"
    print(sol.countAndSay(5))  # "111221"
