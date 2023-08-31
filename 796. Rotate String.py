'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
'''

from collections import deque


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        q1, q2 = deque(), deque()

        for i in A:
            q1.append(i)

        for i in B:
            q2.append(i)

        """
        We can condense above steps as 
        q1, q2 = deque(A), deque(B)
        """

        i = 0
        while i < len(A):
            q1.append(q1.popleft())
            if q1 == q2:
                return True
            i += 1

        return False


'''
Runtime
Details
37ms
Beats 76.09%of users with Python3
Memory
Details
16.38MB
Beats 29.85%of users with Python3
'''
