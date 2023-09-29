'''
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

 

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
 

Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
'''


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If desiredTotal is less than or equal to zero, then player 1 wins
        if desiredTotal <= 0:
            return True
        # If the sum of all the integers is less than the desiredTotal, then player 1 can't win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        # Store the sub-problems result
        self.memo = {}

        # Traverse through all possible moves of player 1
        return self.can_win(tuple(range(1, maxChoosableInteger+1)), desiredTotal)

    def can_win(self, choices, target):
        # If there is only one choice left and it's value is greater than or equal to target, then player 1 wins
        if choices[-1] >= target:
            return True

        # If the sub-problem already exists, return it's result
        if choices in self.memo:
            return self.memo[choices]

        # Traverse through all possible moves of player 1
        for i in range(len(choices)):
            # Player 1 chooses a number
            if not self.can_win(choices[:i]+choices[i+1:], target-choices[i]):
                # If player 2 can't win, then player 1 can win
                self.memo[choices] = True
                return True

        # If no move of player 1 results in player 1 winning, then player 1 can't win
        self.memo[choices] = False
        return False


'''
Runtime
Details
2093ms
Beats 76.01%of users with Python3
Memory
Details
119.44MB
Beats 87.89%of users with Python3
'''
