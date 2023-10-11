'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the remainders and their corresponding indices
        remainder_dict = {0: -1}
        remainder = 0

        # Traverse through the list
        for i in range(len(nums)):
            # Update the remainder with the current number
            remainder += nums[i]

            # If k is not 0, take the remainder when divided by k
            if k != 0:
                remainder %= k

            # If the current remainder is already in the dictionary,
            # and the difference between the current index and the index
            # of the previous occurrence of the same remainder is at least 2,
            # we have found a subarray whose sum is a multiple of k
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] >= 2:
                    return True
            else:
                # If the current remainder is not in the dictionary,
                # add it with its corresponding index
                remainder_dict[remainder] = i

        # If we have traversed through the whole list and haven't found a subarray,
        # return False
        return False


'''
Runtime
Details
945ms
Beats 38.27%of users with Python3
Memory
Details
36.00MB
Beats 83.57%of users with Python3
'''
