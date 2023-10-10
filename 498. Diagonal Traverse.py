'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        R, C = len(mat), len(mat[0])

        diagonal_dict = defaultdict(list)

        for r in range(R):
            for c in range(C):
                diagonal_dict[r+c].append(mat[r][c])

        ans = []

        key = 0

        while key in diagonal_dict:
            if key % 2:  # odd
                ans.extend(diagonal_dict[key])
            else:  # even
                ans.extend(diagonal_dict[key][::-1])

            key += 1

        return ans


'''
Runtime
Details
171ms
Beats 53.49%of users with Python3
Memory
Details
20.18MB
Beats 35.38%of users with Python3
'''
