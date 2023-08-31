'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


'''
Runtime
Details
37ms
Beats 77.84%of users with Python3
Memory
Details
16.27MB
Beats 56.98%of users with Python3
'''
