'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
'''


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        ans = n//3
        rem = n % 3
        if rem == 1:
            return 3**(ans-1)*2*2
        if rem == 2:
            return 3**(ans)*2
        return 3**ans


'''
Runtime
Details
40ms
Beats 52.51%of users with Python3
Memory
Details
16.04MB
Beats 94.48%of users with Python3
'''
