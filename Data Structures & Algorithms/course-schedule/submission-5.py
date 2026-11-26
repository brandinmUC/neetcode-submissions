class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        seen = set()

        for a, b in prerequisites:
            preMap[a].append(b)
        
        def dfs(course):
            if course in seen:
                return False
            if preMap[course] == []:
                return True

            seen.add(course)
            for b in preMap[course]:
                if not dfs(b):
                    return False
            seen.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True