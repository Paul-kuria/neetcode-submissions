class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS  = len(matrix), len(matrix[0])
        top = 0
        bottom = len(matrix)-1

        # Search the row
        while top <= bottom:
            selection = (top + bottom) // 2
            if target > matrix[selection][-1]:
                top = selection + 1
            elif target < matrix[selection][0]:
                bottom = selection -1 
            else:
                break
        
        if not (top <= bottom):
            return False

        # Search the column
        selection = (top + bottom) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[selection][m]:
                l = m+1
            elif target < matrix[selection][m]:
                r = m - 1
            else:
                return True
        return False
            