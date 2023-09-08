'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xdiff = (coordinates[1][0]-coordinates[0][0])
        ydiff = (coordinates[1][1]-coordinates[0][1])

        for i in range(2, len(coordinates)):
            curxdiff = (coordinates[i][0]-coordinates[i-1][0])
            curydiff = (coordinates[i][1]-coordinates[i-1][1])
            if (xdiff*curydiff != ydiff*curxdiff):
                return False
        return True


'''
Runtime
Details
55ms
Beats 98.48%of users with Python3
Memory
Details
16.62MB
Beats 94.44%of users with Python3
'''
