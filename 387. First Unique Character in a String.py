'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for element, count in c.items():
            if count == 1:
                index = s.index(element)
                return index
                break

        return -1


'''
Runtime
Details
68ms
Beats 97.46%of users with Python3
Memory
Details
16.47MB
Beats 83.11%of users with Python3
'''
