'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        letters = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def backTrack(temp, index):
            if len(temp) == n:
                return temp

            for j in letters[digits[index]]:
                temp += j
                a = backTrack(temp, index+1)
                if a:
                    res.append(a)
                temp = temp[0:-1]

        backTrack('', 0)

        return res


'''
Runtime
Details
39ms
Beats 49.62%of users with Python3
Memory
Details
16.20MB
Beats 89.65%of users with Python3
'''
