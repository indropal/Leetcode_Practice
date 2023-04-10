class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        visited = set()
        """
        We iterate through each grid cell & search for land i.e. 0 once we reach a grid cell with 0
        we want to check if its neighbors are having land or water cells. If we encounter the edges of the 
        grid, we consider the land cell as an invalid island & keep on iterating through the grid.

        For the instance we encounter a land cell (0) which is not adjacent to any of the grid boundaries,
        we run DFS to check for other neighboring land cells while ensuring there aren't any water cells or 
        adjacent grid edges encountered in the search - if they are encountered we break out of the DFS loop
        & start searching other areas of the grid.

        Also, while searching, we maintain a visited hashset which keeps track of the grid cells whicch have 
        already been visited during our search.
        """

        def dfs(r, c):
            # return if we have encountered a closed island or not
            if (r == R or c == C or r < 0 or c < 0):
                # encountered grid edge - return 0 for Not a closed island
                return 0
            if ((r, c) in visited) or (grid[r][c] == 1):
                # if already visited or if water cell, then a closed island
                # as we are either wrapping around the island to come back to cell where we started our search
                # or we have reached the edge of the island where there is a water cell
                # - return 1 for closed island
                return 1

            # include the current cell in visited
            visited.add((r, c))

            # run dfs on the adjacent neighboring cells of the current cell & check if it returns
            # any land cell or marker of closed island
            # the minimum value possible 0 which will not affect our count of closed islands only a postive
            # search is 1 which will increment our count

            return min(dfs(r, c+1), dfs(r, c-1), dfs(r-1, c), dfs(r+1, c))

        
        for r in range(R):
            for c in range(C):
                # if the grid cell is a land cell, then runDFS & for a closed island include in count
                if (grid[r][c] == 0) and ((r, c) not in visited):
                    ans += dfs(r, c)
        
        return ans