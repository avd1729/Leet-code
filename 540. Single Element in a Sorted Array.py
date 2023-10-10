'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:  # only unique element
            return nums[0]

        if nums[0] != nums[1]:  # check first element
            return nums[0]

        for i in range(1, len(nums)-1):  # check elements in middle
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]  # only last element will be left


'''
Runtime
Details
156ms
Beats 61.20%of users with Python3
Memory
Details
25.90MB
Beats 80.27%of users with Python3
'''
