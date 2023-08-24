'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
'''


class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        sum = 0
        for i in n:
            sum += int(i)
        if sum < 10:
            return sum
        else:
            return self.addDigits(sum)


'''
Runtime
53ms
Beats 16.71%of users with Python3

Memory
16.31MB
Beats 22.35%of users with Python3
'''


class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 10:
            output = num // 10 + num % 10
            if output < 10:
                return output
            else:
                return self.addDigits(output)
        else:
            return num


'''
Runtime
39ms
Beats 81.79%of users with Python3

Memory
16.40MB
Beats 22.35%of users with Python3
'''
