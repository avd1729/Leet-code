'''
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
'''


class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}

        def helper(screen, clipboard):
            if (screen, clipboard) in cache:
                return cache[(screen, clipboard)]
            if screen == n:
                return 0
            if screen > n:
                return float("Inf")

            copy_paste = helper(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = helper(screen + clipboard, clipboard) + 1

            cache[(screen, clipboard)] = min(copy_paste, paste)
            return cache[(screen, clipboard)]

        return helper(1, 0)


'''
Runtime
Details
180ms
Beats 40.05%of users with Python3
Memory
Details
27.81MB
Beats 18.84%of users with Python3
'''
