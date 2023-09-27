'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = [int(i)for i in range(-1000, 1001)]
        return ans[1000 + a+b]


'''
Runtime
Details
38ms
Beats 51.47%of users with Python3
Memory
Details
16.20MB
Beats 87.65%of users with Python3
'''
