'''
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
'''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x = 0
        idx = 0
        for i, j in enumerate(arr):
            if j > x:
                idx = i
                x = j
        return idx


'''
Runtime
Details
516ms
Beats 59.12%of users with Python3
Memory
Details
30.99MB
Beats 16.94%of users with Python3
'''
