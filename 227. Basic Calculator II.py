'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''


class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if s == '0':
            return 0
        num, sign, stack = 0, '+', []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            if (not ch.isdigit() and ch != ' ') or i == n-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp % num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = ch
                num = 0
        return sum(stack)


'''
Runtime
Details
110ms
Beats 73.13%of users with Python3
Memory
Details
19.50MB
Beats 43.36%of users with Python3
'''
