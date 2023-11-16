'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
'''


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size = len(nums)  # Number of binary strings in the input list

        # Sort the input list in lexicographical order
        nums.sort()

        pointer = 0  # Pointer to track the expected decimal value for the next binary string

        # Iterate through the sorted binary strings
        for i in range(size):
            # Convert the current binary string to decimal
            decimal_value = int(nums[i], 2)

            # Check if the decimal value matches the expected value
            if decimal_value == pointer:
                pointer += 1
            else:
                # If not, return the binary representation of the expected value with appropriate length
                return format(pointer, f'0{size}b')

        # If no unique binary string is found, return the binary representation of the next expected value
        return format(pointer, f'0{size}b')


'''
Runtime
Details
39ms
Beats 75.95%of users with Python3
Memory
Details
16.42MB
Beats 27.31%of users with Python3
'''
