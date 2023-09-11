'''
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 9 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
 

Constraints:

2 <= n <= 104
'''


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(num):
            while num > 0:
                if num % 10 == 0:
                    return False
                num //= 10
            return True
        for i in range(1, n):
            t = n-i
            if check(t) and check(i):
                return [i, t]


'''
Runtime
Details
31ms
Beats 92.48%of users with Python3
Memory
Details
16.07MB
Beats 99.44%of users with Python3
'''
