'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, swap it with the element at index
                # This effectively moves non-zero elements to the beginning of the list
                nums[i], nums[index] = nums[index], nums[i]
                index += 1


'''
Runtime
143ms
Beats 86.66%of users with Python3

Memory
17.96MB
Beats 47.40%of users with Python3
'''
