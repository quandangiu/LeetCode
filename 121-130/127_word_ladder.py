class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = [(beginWord, 1)]
        
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, length + 1))
        
        return 0
