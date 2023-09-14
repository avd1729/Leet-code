'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''


class Solution:
    def maxPower(self, s):
        cnt = 0
        m = 0
        for i in range(1, len(s)):
            if (s[i-1] == s[i]):
                cnt += 1
                m = max(cnt, m)
            else:
                cnt = 0
        return m + 1


'''
Runtime
Details
43ms
Beats 83.60%of users with Python3
Memory
Details
16.06MB
Beats 100.00%of users with Python3
'''
