'''
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
'''


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(32):
            if Counter(str(n)) == Counter(str(2**i)):
                return True
        return False


'''
Runtime
Details
39ms
Beats 76.44%of users with Python3
Memory
Details
16.06MB
Beats 92.44%of users with Python3
'''
