# 1559. Detect Cycles in 2D Grid
# https://leetcode.com/problems/detect-cycles-in-2d-grid/

# DFS

def containsCycle(self, grid: List[List[str]]) -> bool:
    """
    :type grid: List[List[str]]
    :rtype: bool
    """
    def dfs(node, parent):
        if node in visited: return True
        visited.add(node)
        nx,ny = node
        childs = []
        new_directions = [[nx+1,ny],[nx-1, ny],[nx,ny+1],[nx,ny-1]]
        for cx,cy in new_directions:
            # do the dfs with restrictions on where we can go:
            # -if the new index is in within the same boundaries, and
            # -it has the same grid value, and
            # -the index is not equal to the index of the previous index
            if 0 <= cx < m and 0 <= cy < n and grid[cx][cy] == grid[nx][ny] and (cx,cy) != parent:
                childs.append((cx,cy))
        # search through our possible directions
        for x in childs:
            if dfs(x, node): return True
        return False

    m, n = len(grid), len(grid[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            # only use a cell as the starting positon once
            if (i,j) in visited:
                continue
            # parent argument is for the last index we were at, this is initially None as we havent been anywhere
            if dfs((i,j), None):
                return True
    return False