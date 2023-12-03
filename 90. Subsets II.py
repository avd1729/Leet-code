'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, stack = [], []

        def backtrack(i):
            if i >= len(nums):
                output.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i+1)

            stack.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1)

        backtrack(0)
        return output


'''
Runtime
39
ms
Beats
81.12%
of users with Python3
Memory
16.58
MB
Beats
33.93%
of users with Python3
'''
