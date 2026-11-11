class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        b_len = len(board)

        def backtrack(board, word, row, col, visited):
            visited = visited.copy()
            if not word:
                return True
            
            v = board[row][col]
            c = word[0]
            if v != c:
                return False
                
            visited.add(tuple((row, col)))
            for row_change, col_change in directions:
                nr, nc = row + row_change, col + col_change
                if 0 <= nr < b_len and 0 <= nc < len(board[0]) and ((nr, nc) not in visited):
                    res = backtrack(board, word[1:], nr, nc, visited)
                    if res:
                        return True
                if v == c and not word[1:]:
                    return True
            return False

        for i in range(b_len):
            for j in range(len(board[i])):
                c = board[i][j]
                if c == word[0]:
                    res = backtrack(board, word, i, j, set())
                    if res:
                        return True
        return False
