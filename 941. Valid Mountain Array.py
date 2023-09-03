'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        place = arr.index(max(arr))
        if place == 0 or place == len(arr) - 1:
            return False
        else:
            value = True
            i = 0
            while i < place:
                if arr[i] >= arr[i + 1]:
                    value = False
                    break
                else:
                    i += 1
            i = place + 1
            if value:
                while i < len(arr):
                    if arr[i - 1] <= arr[i]:
                        print(i)
                        return False
                    else:
                        i += 1
            else:
                return False
            return True


'''
Runtime
Details
189ms
Beats 54.77%of users with Python3
Memory
Details
17.57MB
Beats 96.72%of users with Python3
'''
