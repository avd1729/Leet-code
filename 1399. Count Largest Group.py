'''
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
'''


class Solution:

    def countLargestGroup(self, n: int) -> int:

        d = {}

        for i in range(1, n + 1):
            t = sum(map(int, list(str(i))))

            if t not in d:
                d[t] = 1
            else:
                d[t] += 1

        m = max(d.values())

        return sum(1 for i in d.values() if i >= m)


'''
Runtime
Details
96ms
Beats 45.14%of users with Python3
Memory
Details
16.07MB
Beats 99.80%of users with Python3
'''
