'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = [str(i) for i in range(1, n+1)]
        for j in range(2, n+1):
            if j % 3 == 0 and j % 5 == 0:
                lst[j-1] = "FizzBuzz"
            elif j % 3 == 0:
                lst[j-1] = "Fizz"
            elif j % 5 == 0:
                lst[j-1] = "Buzz"
        return lst


'''
Runtime
Details
48ms
Beats 74.77%of users with Python3
Memory
Details
17.36MB
Beats 66.63%of users with Python3
'''
