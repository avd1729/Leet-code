'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        target = len(nums)/3
        lst = [element for element, count in c.items() if count > target]
        return lst


'''
Runtime
Details
101ms
Beats 93.73%of users with Python3
Memory
Details
17.68MB
Beats 71.48%of users with Python3
'''
