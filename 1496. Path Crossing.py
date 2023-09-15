'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
'''


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = [[0, 0]]
        x, y = 0, 0
        for i in path:
            if (i == "N"):
                y += 1
            elif (i == "E"):
                x += 1
            elif (i == "S"):
                y -= 1
            else:
                x -= 1
            if [x, y] in d:
                # check if the position is already visited in the list.....
                return True
            d.append([x, y])
            # update the position...
        return False


'''
Runtime
Details
38ms
Beats 67.98%of users with Python3
Memory
Details
16.32MB
Beats 76.80%of users with Python3
'''
