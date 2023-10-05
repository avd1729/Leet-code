'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''


class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize a list to store the least number of perfect square numbers that sum to the index i
        dp = [0] + [float('inf')] * n

        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            # Iterate through all possible perfect square numbers that are less than or equal to i
            for j in range(1, int(i ** 0.5) + 1):
                # Update the least number of perfect square numbers that sum to i
                dp[i] = min(dp[i], dp[i - j*j] + 1)

        # Return the least number of perfect square numbers that sum to n
        return dp[n]


'''
Runtime
Details
2757ms
Beats 58.46%of users with Python3
Memory
Details
16.24MB
Beats 88.31%of users with Python3
'''
