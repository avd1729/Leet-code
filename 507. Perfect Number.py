'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false
 

Constraints:

1 <= num <= 108
'''


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6, 28, 496, 8128, 33550336]


'''
Runtime
Details
36ms
Beats 93.70%of users with Python3
Memory
Details
16.28MB
Beats 61.00%of users with Python3
'''
