'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
'''


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # Calculate and initialize the prefix sums & suffix_sum array
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        # Calculate the prefix sums & suffix_sum array in one loop
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]

        # Calculate absolute differences and update the result array
        for i in range(n):
            current_absolute_diff = (
                (nums[i] * i) - prefix_sum[i]) + (suffix_sum[i] - (nums[i] * (n - i - 1)))
            result[i] = current_absolute_diff

        return result


'''
Runtime
793
ms
Beats
14.10%
of users with Python3
Memory
31.92
MB
Beats
20.51%
of users with Python3
'''
