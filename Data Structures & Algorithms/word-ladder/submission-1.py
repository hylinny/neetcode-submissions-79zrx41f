class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # all words are of the same length
        # build adjacency list 
        if endWord not in wordList:
            return 0

        words = set(wordList)
        adjList = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                w = word[:i] + '*' + word[i+1:]
                adjList[w].append(word)
        
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
                for j in range(len(word)):
                    w = word[:j] + '*' + word[j+1:]
                    for neighbour in adjList[w]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
        
        return 0