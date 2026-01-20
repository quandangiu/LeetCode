# 49. Group Anagrams
# Difficulty: Medium
# Given an array of strings strs, group the anagrams together.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for s in strs:
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
