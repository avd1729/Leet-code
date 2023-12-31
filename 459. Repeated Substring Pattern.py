'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


'''
Runtime
Details
43ms
Beats 79.40%of users with Python3
Memory
Details
16.24MB
Beats 93.86%of users with Python3
'''


# https://leetcode.com/problems/repeated-substring-pattern/solutions/3938580/99-42-2-approaches-o-n/
