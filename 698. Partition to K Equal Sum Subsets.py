'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i, used, cursum):
            if used == DONE:
                return True

            for j in range(i, N):
                if used & (1 << j) > 0:
                    continue
                if j > 0 and used & (1 << j - 1) == 0 and nums[j] == nums[j - 1]:
                    continue

                if nums[j] + cursum < target:
                    if backtrack(j + 1, used | (1 << j), cursum + nums[j]):
                        return True
                elif nums[j] + cursum == target:
                    if backtrack(0, used | (1 << j), 0):
                        return True

                if i == 0:
                    break
            return False

        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        N = len(nums)
        DONE = (1 << N) - 1
        print(nums)
        return backtrack(0, 0, 0)


'''
Runtime
48
ms
Beats
99.19%
of users with Python3
Memory
17.33
MB
Beats
54.28%
of users with Python3
'''
