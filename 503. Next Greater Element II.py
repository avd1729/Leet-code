'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initialize a stack to keep track of indices of elements we haven't found a next greater element for
        stack = []

        # Initialize the result list to contain all -1s (assuming we won't find any next greater element)
        result = [-1] * len(nums)

        # Loop through the array twice (to handle circularity) and process each element
        for _ in range(2):
            for i in range(len(nums)):
                # Pop elements off the stack if they are less than the current element and update their result
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]

                # Add the current index to the stack
                stack.append(i)

        # Return the result list
        return result


'''
Runtime
Details
172ms
Beats 77.93%of users with Python3
Memory
Details
18.05MB
Beats 66.16%of users with Python3
'''
