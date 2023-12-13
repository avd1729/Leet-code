'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dynamic programming, bottom up
        cache = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]
        # fill in the bottom row
        for col in range(len(word2)+1):
            # base case when word 1 is empty
            cache[len(word1)][col] = len(word2) - col
        # fill in the last column
        for row in range(len(word1)+1):
            # base case when word 2 is empty
            cache[row][len(word2)] = len(word1) - row
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:  # char is equal
                    cache[i][j] = cache[i+1][j+1]
                else:  # char is not equal
                    # check insert, delete, replace, all there directions in the 2d cache array
                    cache[i][j] = min(cache[i+1][j], cache[i]
                                      [j+1], cache[i+1][j+1])+1

        return cache[0][0]


'''
Runtime
123
ms
Beats
62.15%
of users with Python3
Memory
20.04
MB
Beats
36.54%
of users with Python3
'''
