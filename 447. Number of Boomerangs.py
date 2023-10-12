'''
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2
Example 3:

Input: points = [[1,1]]
Output: 0
 

Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for p in points:
            d = {}
            for q in points:
                dist = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                d[dist] = d.get(dist, 0) + 1
            for k in d:
                count += d[k] * (d[k] - 1)
        return count


'''
Runtime
Details
1189ms
Beats 54.26%of users with Python3
Memory
Details
16.59MB
Beats 61.35%of users with Python3
'''
