'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        lst = [i for i in c.values()]
        lst.sort()
        if lst[0] == lst[-1]:
            return True
        return False


'''
Runtime
Details
46ms
Beats 40.38%of users with Python3
Memory
Details
15.82MB
Beats 100.00%of users with Python3
'''
