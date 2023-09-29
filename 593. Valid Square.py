'''
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
 

Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104
'''


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.soln1(p1, p2, p3, p4)

    def soln1(self, p1, p2, p3, p4):
        count = collections.Counter()
        coordinates = [p1, p2, p3, p4]

        for i, (xi, yi) in enumerate(coordinates):
            for xj, yj in coordinates[i+1:]:
                d = (xi-xj)**2 + (yi-yj)**2
                count[d] += 1
                if d == 0 or len(count) > 2:
                    return False

        return len(count) == 2 and all(count[i] in {2, 4} for i in count)


'''
Runtime
Details
36ms
Beats 86.03%of users with Python3
Memory
Details
16.22MB
Beats 75.07%of users with Python3
'''
