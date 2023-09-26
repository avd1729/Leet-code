'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        k = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > k:
                k = nums[i]
            k = k - 1
            if k < 0:
                return False
        return True


'''
Runtime
Details
386ms
Beats 95.33%of users with Python3
Memory
Details
17.40MB
Beats 97.79%of users with Python3
'''
