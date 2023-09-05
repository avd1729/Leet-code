'''
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx = 0
        while (idx+1 < len(s)):
            if (s[idx] == s[idx+1]):
                s = s[:idx]+s[idx+2:]
                if idx > 0:
                    idx -= 1
            else:
                idx += 1
        return s


'''
Runtime
Details
219ms
Beats 9.51%of users with Python3
Memory
Details
16.94MB
Beats 99.22%of users with Python3
'''
