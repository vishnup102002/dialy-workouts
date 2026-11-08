class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited=set()
        q=deque()
        rows,cols=len(grid),len(grid[0])
        max_area=0

        def bfs(ro,co):
            q = deque([(ro, co)])
            visited.add((ro, co))
            area = 1
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+row,dc+col
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                        area+=1
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna