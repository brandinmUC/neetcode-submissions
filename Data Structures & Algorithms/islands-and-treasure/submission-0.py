class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        res_grid = [[-2] * len(grid)] * len(grid[0])

        INF = 2**31 - 1
        directions = [[0,1], [1,0], [-1, 0], [0, -1]]
        q = deque()
        seen = set()

        for r_idx in range(len(grid)):
            for c_idx in range(len(grid[0])):
                if grid[r_idx][c_idx] == 0:
                    coord = (r_idx, c_idx, 0)
                    q.append(coord)
        
        while q:
            qr, qc, val = q.popleft()
            if (qr, qc) not in seen:
                seen.add((qr, qc))
                grid[qr][qc] = val
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != -1:
                        q.append((nr, nc, min(val + 1, grid[nr][nc])))

                