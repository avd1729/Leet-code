'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        res, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(count, res)
                count = 0

        return res


'''
Runtime
Details
291ms
Beats 92.92%of users with Python3
Memory
Details
16.58MB
Beats 65.99%of users with Python3
'''
