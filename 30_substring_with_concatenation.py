# 30. Substring with Concatenation of All Words
# Difficulty: Hard
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            current_freq = Counter()
            count = 0
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                
                if word in word_freq:
                    current_freq[word] += 1
                    count += 1
                    
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        result.append(left)
                else:
                    current_freq.clear()
                    count = 0
                    left = j + word_len
        
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # [0, 9]
    print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # []
    print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6, 9, 12]
