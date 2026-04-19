class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(length):
            for c in range(length):
                val = board[r][c]
                if val == ".":
                    continue
                
                # 1. Check rows 
                if (val in rows[r] or val in cols[c] or val in squares[(r//3), c//3]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[r//3, c//3].add(val)
        return True
                