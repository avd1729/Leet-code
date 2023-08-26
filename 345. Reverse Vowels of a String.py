'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = ["a", "e", "i", "o", "u"]
        val = []
        pos = []
        for i in range(len(s)):
            if s[i].lower() in v:
                val.append(s[i])
                pos.append(i)
        val = val[::-1]
        for i in range(len(pos)):
            s[pos[i]] = val[i]
        return ''.join(s)


'''
Runtime
Details
53ms
Beats 86.88%of users with Python3
Memory
Details
19.22MB
Beats 6.51%of users with Python3
'''
