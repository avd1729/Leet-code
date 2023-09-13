'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
'''


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        dim = len(mat)
        for i in range(dim):
            sum += mat[i][i]
            sum += mat[i][dim-1-i]
        if dim % 2 == 1:
            diff = mat[dim//2][dim//2]
            return sum - diff
        return sum


'''
Runtime
Details
97ms
Beats 93.36%of users with Python3
Memory
Details
16.44MB
Beats 97.08%of users with Python3
'''
