from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
