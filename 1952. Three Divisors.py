'''
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.

 

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
 

Constraints:

1 <= n <= 104
'''


class Solution:
    def isThree(self, n: int) -> bool:
        count = 2  # one and the number itself
        for i in range(2, (n//2)+1):
            if n % i == 0:
                count += 1
        if count == 3:
            return True
        return False


'''
Runtime
Details
35ms
Beats 88.90%of users with Python3
Memory
Details
16.13MB
Beats 84.83%of users with Python3
'''
