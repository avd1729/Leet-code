'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''


class Solution:
    def maximumSwap(self, num):
        num = list(str(num))
        max_idx = len(num) - 1
        small = large = 0

        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i  # this is the right side max number index
            elif num[i] < num[max_idx]:
                small = i
                large = max_idx

        num[small], num[large] = num[large], num[small]
        return int(''.join(num))  # join a list of string/charaters


'''
Runtime
Details
40ms
Beats 42.15%of users with Python3
Memory
Details
16.21MB
Beats 50.96%of users with Python3
'''
