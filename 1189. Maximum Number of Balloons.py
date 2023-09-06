'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''


class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        return min(s.count('b'), s.count('a'), s.count('l')//2, s.count('o')//2, s.count('n'))


'''
Runtime
Details
41ms
Beats 69.04%of users with Python3
Memory
Details
16.23MB
Beats 90.83%of users with Python3
'''
