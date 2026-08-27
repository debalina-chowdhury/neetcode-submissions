from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def addCell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
            dist += 1
    #O(m*n), O(m*n)
