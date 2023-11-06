'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # In constant O(1) space
        incre, decre, ans = 0, 0, 0
        for i in range(1, len(arr)):
            if (decre and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                incre, decre = 0, 0
            incre += arr[i-1] < arr[i]
            decre += arr[i-1] > arr[i]

            if incre and decre:
                ans = max(ans, incre + decre + 1)
        return ans


'''
Runtime
Details
150ms
Beats 59.64%of users with Python3
Memory
Details
17.48MB
Beats 57.19%of users with Python3
'''
