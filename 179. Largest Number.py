'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return '0'

        nums = list(map(str, nums))
        if len(nums) < 2:
            return "".join(nums)

        def compare(x, y):
            return (int(nums[x]+nums[y])) > (int(nums[y]+nums[x]))

        for x in range(len(nums) - 1):
            y = x + 1
            while x < len(nums) and y < (len(nums)):
                if not compare(x, y):
                    nums[y], nums[x] = nums[x], nums[y]
                y += 1

        return "".join(nums)


'''
Runtime
Details
87ms
Beats 6.15%of users with Python3
Memory
Details
16.09MB
Beats 98.53%of users with Python3
'''
