from collections import Counter

class Solution:
    def findSubstring(self, s, words):
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
