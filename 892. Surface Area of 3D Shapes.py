'''
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

 

Example 1:


Input: grid = [[1,2],[3,4]]
Output: 34
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 3:


Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
'''


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        l = len(grid)
        area = 0
        for row in range(l):
            for col in range(l):
                if grid[row][col]:
                    # surface area of each block if blocks werent connected
                    area += (grid[row][col]*4) + 2
                if row:  # row>0
                    # subtracting as area is common among two blocks
                    area -= min(grid[row][col], grid[row-1][col])*2
                if col:  # col>0
                    # subtracting as area is common among two blocks
                    area -= min(grid[row][col], grid[row][col-1])*2
        return area


'''
Runtime
Details
79ms
Beats 82.29%of users with Python3
Memory
Details
16.42MB
Beats 38.75%of users with Python3
'''
