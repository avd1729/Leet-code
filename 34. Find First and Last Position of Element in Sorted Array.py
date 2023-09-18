'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for idx, i in enumerate(nums):
            if i == target:
                lst.append(idx)
        if len(lst) == 0:
            return [-1, -1]
        elif len(lst) == 1:
            return [lst[0], lst[0]]
        else:
            return [lst[0], lst[-1]]


'''
Runtime
Details
82ms
Beats 73.72%of users with Python3
Memory
Details
17.69MB
Beats 93.43%of users with Python3
'''
