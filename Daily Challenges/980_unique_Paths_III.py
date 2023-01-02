class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        sx = sy = ex = ey = None
        empty = 0

        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    sx, sy  = x, y

                elif grid[x][y] == 2:
                    ex, ey = x, y

                if grid[x][y] != -1:
                    empty += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def count(x, y, seen):
            if x == ex and y == ey:
                if len(seen) == empty:
                    return 1

                else:
                    return 0

            total = 0
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < R) and (0 <= ny < C) and grid[nx][ny]!=-1 and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    total += count(nx, ny, seen)
                    seen.remove((nx, ny))

            return total

        return count(sx, sy, set([(sx, sy)]))