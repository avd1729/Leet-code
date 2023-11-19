'''
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

 

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]
 

Constraints:

1 <= n <= 1000
'''


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            odd = [2*i-1 for i in res]
            even = [2*i for i in res]
            res = odd+even
        return [i for i in res if i <= n]


'''
Runtime
37
ms
Beats
84.33%
of users with Python3
Memory
16.45
MB
Beats
38.06%
of users with Python3
'''
