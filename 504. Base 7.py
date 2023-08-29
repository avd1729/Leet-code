'''
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        result = ""
        n = abs(num)
        while n:
            result += str(n % 7)
            n //= 7
        if num < 0:
            result += '-'
        return result[::-1]


'''
Runtime
Details
42ms
Beats 53.52%of users with Python3
Memory
Details
16.18MB
Beats 90.30%of users with Python3
'''
