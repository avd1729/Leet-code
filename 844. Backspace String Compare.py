'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = '', ''
        for i in s:
            if i != '#':
                a += i
            else:
                a = a[:-1]
        for j in t:
            if j != '#':
                b += j
            else:
                b = b[:-1]
        return a == b


'''
Runtime
Details
47ms
Beats 28.75%of users with Python3
Memory
Details
16.18MB
Beats 95.08%of users with Python3
'''
