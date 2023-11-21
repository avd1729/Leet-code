'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''


class Solution:
    def reverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def countNicePairs(self, nums: List[int]) -> int:
        mod = 1000000007

        nums = [num - self.reverse(num) for num in nums]
        nums.sort()

        res = 0
        i = 0
        while i < len(nums) - 1:
            cont = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                cont += 1
                i += 1
            res = (res % mod + (cont * (cont - 1)) // 2) % mod
            i += 1

        return int(res % mod)


'''
Runtime
675
ms
Beats
18.13%
of users with Python3
Memory
26.89
MB
Beats
33.99%
of users with Python3
'''
