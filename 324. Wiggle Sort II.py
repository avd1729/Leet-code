'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]


'''
Runtime
Details
146ms
Beats 51.22%of users with Python3
Memory
Details
19.12MB
Beats 76.52%of users with Python3
'''
