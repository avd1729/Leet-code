'''
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:

1 <= n <= 250
'''


class Solution:

    def countTriples(self, n: int) -> int:

        res = 0

        for i in range(1, n):
            for j in range(i + 1, n):
                s = math.sqrt(i * i + j * j)
                if int(s) == s and s <= n:
                    res += 2

        return res


'''
Runtime
Details
194ms
Beats 77.61%of users with Python3
Memory
Details
16.21MB
Beats 67.16%of users with Python3
'''
