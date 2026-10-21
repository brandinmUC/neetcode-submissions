class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        seen = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # optimized neighbor check
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = collections.deque()
            seen.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions: # directional row, directional col
                    nr, nc = dr + row, dc + col #new row, new col
                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    grid[nr][nc] == "1" and 
                    (nr, nc) not in seen):
                        queue.append((nr, nc))
                        seen.add((nr, nc))

        for row in range(rows):
            for col in range(cols):
                val = grid[row][col]
                if val == "1" and ((row, col) not in seen):
                    bfs(row, col)
                    res += 1

        return res

    