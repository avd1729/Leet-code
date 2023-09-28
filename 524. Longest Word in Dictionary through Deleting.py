'''
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
'''


class Solution:
    def findLongestWord(self, S: str, D: List[str]) -> str:
        ans = ""
        for word in D:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans):
                continue
            pos = -1
            for char in word:
                pos = S.find(char, pos + 1)
                if pos == -1:
                    break
            else:
                ans = word
        return ans


'''
Runtime
Details
68ms
Beats 100.00%of users with Python3
Memory
Details
18.84MB
Beats 51.09%of users with Python3
'''
