'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])

        def bk(start, sub):  # bk stands for backtracking
            for i in range(start, len(nums)):
                sub.append(nums[i])
                ans.append(sub.copy())
                bk(i+1, sub)
                sub.pop()
        bk(0, [])
        return ans


'''
Runtime
Details
34ms
Beats 91.37%of users with Python3
Memory
Details
16.34MB
Beats 88.03%of users with Python3
'''
