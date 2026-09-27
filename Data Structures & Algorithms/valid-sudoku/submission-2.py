class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rset = set()
            for val in row:
                if val == ".":
                    continue
                if val in rset:
                    return False
                else:
                    rset.add(val)

        for col in range(9):
            cset = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in cset:
                    return False
                else:
                    cset.add(val)

        for square in range(9):
            sset = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square% 3) * 3 + j
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in sset:
                        return False
                    else:
                        sset.add(val)
        return True
                
        