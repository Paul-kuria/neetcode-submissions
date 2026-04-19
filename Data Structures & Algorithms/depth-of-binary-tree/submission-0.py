class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If tree is empty
        if not root:
            return 0
        
        # Initialize deque & counter        
        queue = deque([root])
        depth = 0
        counter = []

        # While queue 
        while queue:
            lenth_queue = len(queue)
            current_level = []

            for _ in range(lenth_queue):
                curr = queue.popleft()
                # Add values for current level
                current_level.append(curr.val)
                
                # ADD Children to the back of the line
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            counter.append(current_level)
        
        return len(counter)
        i = 0
        while i < len(counter):
            ans.append(counter[i])
            i += 1
            if counter[i] is None:
                return len(ans)