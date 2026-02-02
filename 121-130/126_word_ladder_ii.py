class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Build adjacency list
        from collections import defaultdict
        neighbors = defaultdict(list)
        
        def get_neighbors(word):
            if word in neighbors:
                return neighbors[word]
            result = []
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet and next_word != word:
                        result.append(next_word)
            neighbors[word] = result
            return result
        
        # BFS to find shortest distance
        level = {beginWord: 0}
        parent = defaultdict(list)
        queue = [beginWord]
        step = 0
        found = False
        
        while queue and not found:
            step += 1
            next_queue = []
            for word in queue:
                for next_word in get_neighbors(word):
                    if next_word not in level:
                        level[next_word] = step
                        next_queue.append(next_word)
                    
                    if level[next_word] == step:
                        parent[next_word].append(word)
                    
                    if next_word == endWord:
                        found = True
            
            queue = next_queue
        
        if not found:
            return []
        
        # Backtrack to build paths
        result = []
        
        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            
            for prev in parent[word]:
                path.append(prev)
                backtrack(prev, path)
                path.pop()
        
        backtrack(endWord, [endWord])
        return result
