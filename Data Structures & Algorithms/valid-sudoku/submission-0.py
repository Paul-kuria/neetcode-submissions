class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = len(board)
        horizontal = len(board[0])

        rows = {}
        cols = {}
        
        
        # Check Rows
        for r in range(horizontal):
            seen_in_row = set()
            for c in range(vertical):
                num = board[r][c]

                if num == ".":
                    continue 
                # Check for duplicate and return immediately
                if num in seen_in_row:
                    return False 
                seen_in_row.add(num)
         
        # Check Columns
        for c in range(vertical):
            seen_in_col = set()
            for r in range(horizontal):
                num = board[r][c]
                if num == ".":
                    continue
                if num in seen_in_col:
                    return False 
                
                seen_in_col.add(num)

        # Check 3x3 Grid 
        seen_in_boxes = defaultdict(set)
        for r in range(horizontal):
            for c in range(vertical):
                num = board[r][c]
                if num == ".":
                    continue
                box_row = r // 3
                box_col = c // 3
                box_key = (box_row, box_col)

                if num in seen_in_boxes[box_key]:
                    return False 
                seen_in_boxes[box_key].add(num)

        return True
