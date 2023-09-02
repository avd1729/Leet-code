'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets = [i for i in s if i.isalpha()][-1::-1]
        for i in range(len(s)):
            if not (s[i].isalpha()):
                alphabets.insert(i, s[i])
        alphabets = ''.join(alphabets)
        return alphabets


'''
Runtime
Details
40ms
Beats 61.28%of users with Python3
Memory
Details
16.21MB
Beats 66.47%of users with Python3
'''
