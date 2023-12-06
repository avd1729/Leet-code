'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        if n < 2:
            res[0][0] = 1
            return res
        else:
            track = 1
            cycle = 1
            k = 0
            i = 0
            while k < n:
                # For 1st Cycle --> Left to Right
                if cycle == 1:
                    for j in range(k, n):
                        res[i][j] = track
                        track += 1

                # For 2nd Cycle --> Top to Bottom
                if cycle == 2:
                    for j in range(k+1, n):
                        res[j][i] = track
                        track += 1

                # For 3rd Cycle --> Right to Left
                if cycle == 3:
                    for j in range(n-2, k-1, -1):
                        res[i][j] = track
                        track += 1

                # For 4th Cycle --> Bottom to Top
                if cycle == 4:
                    for j in range(n-2, k, -1):
                        res[j][i] = track
                        track += 1
                i = j
                if cycle == 4:
                    cycle = 1
                    k += 1
                    n -= 1
                else:
                    cycle += 1

        return res


'''
Runtime
41
ms
Beats
45.82%
of users with Python3
Memory
16.30
MB
Beats
64.02%
of users with Python3
'''
