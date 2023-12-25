'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def subset(p, up):
            if len(up) == 0:
                if p not in ans:
                    ans.append(p)
                return
            ch = up[0]
            for i in range(len(p) + 1):
                subset(p[0:i] + [ch] + p[i:], up[1:])
        subset([], nums)
        return ans


'''
Runtime
602
ms
Beats
11.09%
of users with Python3
Memory
17.59
MB
Beats
9.84%
of users with Python3
'''
