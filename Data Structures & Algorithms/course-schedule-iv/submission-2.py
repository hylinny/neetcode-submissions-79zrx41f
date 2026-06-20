class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prereq [ai, bi] : graph bi -> ai
        # for each query, try traversing graph and see if
        # we can reach uj from vj
        adjList = defaultdict(list)
        for prereq, course in prerequisites:
            adjList[course].append(prereq)

        def dfs(course, prereq, visited):
            # check if prereq ever exists in dfs call
            if course == prereq:
                return True
            for neighbour in adjList[course]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if dfs(neighbour, prereq, visited):
                        return True
            return False
        
        output = []
        for prereq, course in queries:
            visited = set()
            output.append(dfs(course, prereq, visited))

        return output