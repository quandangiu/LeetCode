class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = {}
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer.setdefault(newWord, []).extend([path + [newWord] for path in layer[word]])
            
            wordSet -= set(newlayer.keys())
            layer = newlayer
        
        return []
