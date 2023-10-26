'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convert(time):
            h = int(time[:2])
            m = int(time[3:])
            return h*60 + m

        l = [convert(t) for t in timePoints]
        l.sort()
        n = len(l)

        res = min(l[i+1]-l[i] for i in range(n-1))

        return min(res, 1440-l[-1]+l[0])  # Think in anticlockwise


'''
Runtime
Details
64ms
Beats 97.59%of users with Python3
Memory
Details
19.52MB
Beats 54.16%of users with Python3
'''
