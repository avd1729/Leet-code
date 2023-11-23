'''
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
'''


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] = 1 - grid[row][col]

        for col in range(1, n):
            num_bit_ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    num_bit_ones += 1
            if num_bit_ones < m - num_bit_ones:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for col in range(n):
            num_bit_ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    num_bit_ones += 1

            score += num_bit_ones * 2 ** (n-1 - col)

        return score


'''
Runtime
44
ms
Beats
59.28%
of users with Python3
Memory
16.36
MB
Beats
20.36%
of users with Python3
'''
