'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
'''


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        try:
            l = int(log2(max(nums)))
        except:
            l = 1

        mask, res = 0, 0

        for i in range(l, -1, -1):
            mask |= 1 << i
            S = set(mask & num for num in nums)
            temp = res | 1 << i

            for num in S:
                if num ^ temp in S:
                    res = temp
                    break

        return res


'''
Runtime
Details
1422ms
Beats 73.93%of users with Python3
Memory
Details
65.39MB
Beats 78.75%of users with Python3
'''
