'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # if the characters match, move the pointer for s
                i += 1
            j += 1  # move the pointer for t regardless
        # if i has reached the end of s, s is a subsequence of t, else not
        return i == len(s)


'''
Runtime
Details
43ms
Beats 59.21%of users with Python3
Memory
Details
16.33MB
Beats 61.48%of users with Python3
'''
