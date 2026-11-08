"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapp={}
        def dfs(c_node):
            if c_node in mapp:
                return mapp[c_node]
            copy=Node(c_node.val)
            mapp[c_node]=copy
            for neighbor in c_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna