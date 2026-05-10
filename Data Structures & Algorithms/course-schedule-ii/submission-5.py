class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # toposort
        # take course b before course a
        # if cycle detected, return []
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        output = []
        visited = set()
        visiting = set()
        def dfs(i):
            if i in visiting:
                return False
            visiting.add(i)
            courses = adjList[i]
            for course in courses:
                if course not in visited and not dfs(course):
                    return False
            visited.add(i)
            visiting.remove(i)
            output.append(i)
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        output.reverse()
        return output
        

