from collections import deque

class Solution:
    def invertTree(self, root):
        # Case: If the tree is empty, return None (not an empty list!)
        if not root:
            return None
        
        # Initialize our roller coaster line with the root inside a list!
        queue = deque([root])

        while queue:
            # 1. The current node gets out of line
            current = queue.popleft()

            # 2. THE SECRET SAUCE: Physically swap its left and right children
            # This is standard Python syntax for swapping two variables
            current.left, current.right = current.right, current.left

            # 3. Send the children to the back of the line so they can swap their kids later
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        # Return the top of the newly modified tree
        return root