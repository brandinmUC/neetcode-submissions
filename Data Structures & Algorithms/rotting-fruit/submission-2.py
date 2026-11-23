class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        fresh = set()
        q = deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 0
        rotten = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coord = (row, col)
                if grid[row][col] == 2:
                    rotten.append(coord)
                if grid[row][col] == 1:
                    fresh.add(coord)
        q.append(rotten)
                    
        
        while q:
            level = q.popleft() # each rotten banana at that minute (in a lst)
            n_rotten = []
            for qr, qc in level:
                if (qr, qc) in fresh:
                    fresh.remove((qr, qc))
                if (qr, qc) not in seen:
                    seen.add((qr, qc))
                    for dr, dc in directions:
                        nr, nc = qr + dr, qc + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            n_rotten.append((nr, nc))
                    
            if n_rotten:
                q.append(n_rotten)
                res += 1
                    
        return -1 if fresh else res