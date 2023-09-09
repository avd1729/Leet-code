'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
'''

import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # step 1: count the dominoes
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c


'''
Runtime
Details
212ms
Beats 90.89%of users with Python3
Memory
Details
26.15MB
Beats 72.48%of users with Python3
'''
