'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeTwoSortedArrays(a, b, res):
            i, j, k = 0, 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res[k] = a[i]
                    i += 1
                else:
                    res[k] = b[j]
                    j += 1
                k += 1

            res[k:] = a[i:] if i < len(a) else b[j:]

        def mergesort(nums):
            if len(nums) == 1:
                return
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]

            mergesort(L)
            mergesort(R)

            mergeTwoSortedArrays(L, R, nums)

        mergesort(nums)
        return nums


'''
Runtime
Details
1463ms
Beats 65.40%of users with Python3
Memory
Details
23.99MB
Beats 68.35%of users with Python3
'''
