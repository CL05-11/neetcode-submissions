class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  using DFS and can map courses with prerequistis and also have visit set
        preMap = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preMap[c].append(p)

        VS = set()
        def dfs(c):
            if c in VS:
                return False
            if preMap[c] == []:
                return True
            VS.add(c)
            for p in preMap[c]:
                if not dfs(p): return False

            VS.remove(c)
            preMap[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True

