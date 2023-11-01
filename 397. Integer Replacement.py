'''
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
 

Constraints:

1 <= n <= 231 - 1
'''


class Solution:
    def integerReplacement(self, n: int) -> int:
        # Initialize the memoization dictionary
        memo = {}
        # Call the recursive function
        return self.helper(n, memo)

    def helper(self, n, memo):
        # Base case: if n is 1, return 0
        if n == 1:
            return 0
        # Check if the result is already memoized
        if n in memo:
            return memo[n]
        # If n is even, divide it by 2 and make a recursive call
        if n % 2 == 0:
            memo[n] = 1 + self.helper(n // 2, memo)
        # If n is odd, make two recursive calls for n+1 and n-1 and return the minimum of the two values
        else:
            memo[n] = 1 + min(self.helper(n + 1, memo),
                              self.helper(n - 1, memo))
        # Return the memoized result
        return memo[n]


'''
Runtime
Details
36ms
Beats 82.43%of users with Python3
Memory
Details
16.26MB
Beats 56.12%of users with Python3
'''
