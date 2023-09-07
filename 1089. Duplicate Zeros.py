'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        a = []
        for i in range(len(arr)):
            if arr[i] == 0:
                a.append(i)
        k = 0
        for i in range(len(a)):
            arr.insert(a[i]+k, 0)
            k += 1
        m = len(arr)
        for i in range(m-n):
            arr.pop()
        return arr


'''
Runtime
Details
75ms
Beats 52.12%of users with Python3
Memory
Details
17.14MB
Beats 60.56%of users with Python3
'''
