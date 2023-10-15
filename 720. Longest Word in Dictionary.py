'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
'''


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        buildable = set()

        for w in words:
            pre = w[:-1]
            if not pre or pre in buildable:
                buildable.add(w)

        res = ''
        for w in buildable:
            if len(w) > len(res) or (len(w) == len(res) and w < res):
                res = w
        return res


'''
Runtime
Details
87ms
Beats 79.29%of users with Python3
Memory
Details
16.82MB
Beats 69.44%of users with Python3
'''
