class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # all words are of the same length
        # build adjacency list 
        if endWord not in wordList:
            return 0

        def transformable(word1, word2):
            mismatches = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    mismatches += 1
            return mismatches == 1

        words = set()
        words.add(beginWord)
        words.add(endWord)
        words.update(wordList)
        adjList = defaultdict(list)
        for word1 in words:
            for word2 in words:
                if transformable(word1, word2):
                    adjList[word1].append(word2)
                    adjList[word2].append(word1)
        
        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        transformations = 0
        while queue:
            frontier = len(queue)
            transformations += 1
            for i in range(frontier):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for neighbour in adjList[word]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        return 0