'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
'''


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # variable to keep track of the number of modifications
        count = 0
        # iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # check if the current element is less than the previous element
            if nums[i] < nums[i-1]:
                # if it is, increment the count
                count += 1
                # if we have already made a modification, return False
                if count > 1:
                    return False
                # if the current element is less than or equal to the element before the previous element
                # we modify the current element to be equal to the previous element
                if i < 2 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                # otherwise, we modify the previous element to be equal to the current element
                else:
                    nums[i] = nums[i-1]
        # if we reach the end of the loop without returning False, return True
        return True


'''
Runtime
Details
166ms
Beats 65.58%of users with Python3
Memory
Details
17.72MB
Beats 42.36%of users with Python3
'''
