'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        return sum(bisect_left(nums, nums[i]+nums[j]) - j-1 for i in range(len(nums)-2) if nums[i] != 0 for j in range(i+1, len(nums)-1))


'''
Runtime
Details
1475ms
Beats 35.49%of users with Python3
Memory
Details
16.22MB
Beats 85.64%of users with Python3
'''
