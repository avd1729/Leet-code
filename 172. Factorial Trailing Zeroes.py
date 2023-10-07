'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
'''


class Solution(object):
    def trailingZeroes(self, n):
        # Negative Number Edge Case
        if (n < 0):
            return -1
        # Initialize output...
        output = 0
        # Keep dividing n by 5 & update output...
        while (n >= 5):
            n //= 5
            output += n
        return output    # Return the output...


'''
Runtime
Details
40ms
Beats 65.57%of users with Python3
Memory
Details
16.06MB
Beats 95.71%of users with Python3
'''
