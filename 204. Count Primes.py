'''
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        prime = [True] * (n+1)
        prime[0], prime[1] = False, False

        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False

        res = [i for i in range(2, n) if prime[i]]

        return len(res)


'''
Runtime
Details
2215ms
Beats 52.02%of users with Python3
Memory
Details
68.76MB
Beats 47.39%of users with Python3
'''
