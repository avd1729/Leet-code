'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
'''


class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        for char in s:
            if char.isdigit():
                nums.append(int(char))
        nums = [num for num in nums if num != max(nums)]
        if len(nums) >= 1:
            return max(nums)
        else:
            return -1


'''
Runtime
Details
72ms
Beats 5.83%of users with Python3
Memory
Details
16.07MB
Beats 99.47%of users with Python3
'''
