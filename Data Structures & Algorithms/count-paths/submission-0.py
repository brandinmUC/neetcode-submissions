class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[0, 1], [1, 0]]

        grid = [[0 for row in range(n)] for col in range (m)]
        grid[-1] = [1] * n

        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if (nr in range(m) and 
                    nc in range(n)): 
                        grid[i][j] += grid[nr][nc]

        return grid[0][0]
