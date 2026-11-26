class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        seen = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def capture(r, c):
            if (r < 0 or c < 0 or r == len(board) or c == len(board[0]) 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                capture(nr, nc)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row in [0, len(board) - 1] 
                or col in [0, len(board[0]) - 1]):
                    capture(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                v = board[row][col]
                if v == "T":
                    board[row][col] = "O"
                if v == "O":
                    board[row][col] = "X"
   