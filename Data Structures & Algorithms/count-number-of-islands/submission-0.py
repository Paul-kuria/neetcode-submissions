class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0 

        def dfs(r, c):
            # 1. Base case: Are we out of bounds or at a water/visited cell?
            if (r < 0 or r >= rows 
                or c < 0 or c >= cols 
                or grid[r][c] == "0"):
                return
            
            # 2. Mark the current cell as visited (sink it!)
            grid[r][c] = "0" 

            # 3. Explore the neighbors (U, D, L, R)
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r , c - 1) # Left 
        
        # Main loop: Scan entire board
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # We found a new Island!
                    islands += 1 
                    # Use DFS to "sink" all connected parts of this island
                    dfs(r, c)
        return islands