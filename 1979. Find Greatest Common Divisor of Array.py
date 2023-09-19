'''
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
 

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        l = nums[0]
        r = nums[-1]
        gcd = 1
        for i in range(2, l+1):
            if l % i == 0 and r % i == 0:
                gcd = max(i, gcd)
        return gcd


'''
Runtime
Details
52ms
Beats 93.33%of users with Python3
Memory
Details
16.47MB
Beats 55.05%of users with Python3
'''
