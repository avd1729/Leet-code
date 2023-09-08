'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105
'''

from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        return c.most_common(1)[0][0]


'''
Runtime
Details
90ms
Beats 76.09%of users with Python3
Memory
Details
18.09MB
Beats 23.66%of users with Python3
'''
