'''
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
'''


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(y):
            if y == 1:
                return False
            for i in range(2, y//2+1):
                if y % i == 0:
                    return False
            return True
        c = 0
        for i in range(1, n+1):
            if isPrime(i) == True:
                c += 1

        def fac(x):
            f = 1
            while x > 0:
                f = (f*x) % (10**9+7)
                x -= 1
            return f
        return fac(n-c)*fac(c) % (10**9+7)


'''
Runtime
Details
38ms
Beats 68.46%of users with Python3
Memory
Details
16.16MB
Beats 91.95%of users with Python3
'''
