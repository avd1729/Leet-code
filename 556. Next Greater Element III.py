'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
'''


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        flag = False
        for i in range(len(s)-1, 0, -1):
            if s[i-1] < s[i]:
                j = -1
                while s[i-1] >= s[j]:
                    j -= 1
                s[i-1], s[j] = s[j], s[i-1]
                s[i:] = sorted(s[i:])
                flag = True
                break
        m = int(''.join(s))
        if m >= 2**31 or m < 1 or not flag:
            return -1
        else:
            return m


'''
Runtime
Details
41ms
Beats 32.85%of users with Python3
Memory
Details
16.10MB
Beats 96.65%of users with Python3
'''
