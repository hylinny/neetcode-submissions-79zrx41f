class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # each prerequisite entry represents a directed edge from b to a
        # just need to detect cycles, since graph is always connected
        # dfs with cycle detection
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            
            visited.add(course)
            for neighbour in adj[course]:
                if not dfs(neighbour):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        
        for i in range(numCourses): # iterate through adjacency list
            if not dfs(i):
                return False
        return True

        