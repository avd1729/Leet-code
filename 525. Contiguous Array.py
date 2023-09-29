'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        ps = 0
        prefix_sum_at_idx = {0: 0}
        for i, n in enumerate(nums):
            ps = ps+1 if n == 1 else ps-1

            if ps in prefix_sum_at_idx:
                res = max(res, i - prefix_sum_at_idx[ps] + 1)
            else:
                prefix_sum_at_idx[ps] = i+1

        return res


'''
Runtime
Details
700ms
Beats 50.98%of users with Python3
Memory
Details
21.54MB
Beats 78.23%of users with Python3
'''
