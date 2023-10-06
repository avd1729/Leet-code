'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 231 - 1
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:  # If n is a single digit, return n
            return n

        base = 9  # Set the base value for the digit count
        digits = 1  # Set the initial number of digits to 1
        while n > base * digits:
            n -= base * digits  # Subtract the count of digits from n
            base *= 10  # Increase the base value by a factor of 10
            digits += 1  # Increase the number of digits by 1

        # Calculate the number where the nth digit is located
        num = 10 ** (digits - 1) + (n - 1) // digits
        # Calculate the index of the nth digit in the number
        idx = (n - 1) % digits

        return int(str(num)[idx])  # Return the nth digit as an integer


'''
Runtime
Details
37ms
Beats 58.86%of users with Python3
Memory
Details
16.21MB
Beats 48.80%of users with Python3
'''
