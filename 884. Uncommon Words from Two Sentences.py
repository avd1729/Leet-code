'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        lst = []
        for i in s1:
            if i not in s2:
                lst.append(i)
        for j in s2:
            if j not in s1:
                lst.append(j)
        c = Counter(lst)
        elements = [element for element, count in c.items() if count == 1]
        return elements


'''
Runtime
Details
36ms
Beats 84.39%of users with Python3
Memory
Details
16.16MB
Beats 95.29%of users with Python3
'''
