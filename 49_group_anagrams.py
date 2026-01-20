# 49. Group Anagrams
# Difficulty: Medium
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    print(sol.groupAnagrams([""]))  # [[""]]
    print(sol.groupAnagrams(["a"]))  # [["a"]]
