'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
'''


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        res = []
        for i in "qwertyuiop":
            dic[i] = 1
        for i in "asdfghjkl":
            dic[i] = 2
        for i in "zxcvbnm":
            dic[i] = 3
        for i in words:
            new = i.lower()
            prev = dic[new[0]]
            flg = 1
            for j in new:
                if dic[j] != prev:
                    flg = 0
                    break
                prev = dic[j]
            if flg == 1:
                res.append(i)
        return res


'''
Runtime
Details
36ms
Beats 83.81%of users with Python3
Memory
Details
16.32MB
Beats 32.92%of users with Python3
'''
