'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1
'''


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        s = s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]


'''
Runtime
Details
34ms
Beats 80.12%of users with Python3
Memory
Details
16.17MB
Beats 86.34%of users with Python3
'''
