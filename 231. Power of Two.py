'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        lst = []
        for i in range(0, 31):
            lst.append(2**i)
        s = set(lst)
        if n in s:
            return True
        return False


'''
Runtime
36ms
Beats 89.35%of users with Python3

Memory
16.26MB
Beats 61.03%of users with Python3
'''
