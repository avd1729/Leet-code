'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
'''

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        c2.subtract(c1)
        return c2.most_common(1)[0][0]


'''
Runtime
Details
35ms
Beats 94.45%of users with Python3
Memory
Details
16.37MB
Beats 52.23%of users with Python3
'''
