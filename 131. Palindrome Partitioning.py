'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''


class Solution:
    def dp(self, i, s, st):
        if i >= len(s):
            self.lst.append(tuple(st))
            return
        for j in range(i, len(s)):
            if s[i:j+1] == ''.join(reversed(s[i:j+1])):
                st.append(s[i:j+1])
                x = self.dp(j+1, s, st)
                st.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        self.lst = []
        self.dp(0, s, [])
        return self.lst


'''
Runtime
Details
549ms
Beats 59.54%of users with Python3
Memory
Details
30.04MB
Beats 99.37%of users with Python3
'''
