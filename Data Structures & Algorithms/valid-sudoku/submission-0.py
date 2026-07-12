class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # there is 9X9 grid and we need to follow rules by each row and col and see 3x3 grids as well
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sdk = collections.defaultdict(set) # key =. (r/3,c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sdk[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sdk[(r//3,c//3)].add(board[r][c])
        return True
