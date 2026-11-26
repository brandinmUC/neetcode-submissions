class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                capture(nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS - 1] 
                or col in [0, COLS - 1]):
                    capture(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                v = board[row][col]
                if v == "T":
                    board[row][col] = "O"
                elif v == "O":
                    board[row][col] = "X"
   