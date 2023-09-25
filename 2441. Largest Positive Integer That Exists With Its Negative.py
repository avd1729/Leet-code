'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
'''


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos, neg = set(), set()
        for digit in nums:
            pos.add(digit) if digit > 0 else neg.add(digit)

        for digit in sorted(pos, reverse=True):
            if (digit*-1) in neg:
                return digit
        return -1


'''
Runtime
Details
118ms
Beats 70.83%of users with Python3
Memory
Details
16.46MB
Beats 73.03%of users with Python3
'''
