'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''

from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # Step 1: Convert nums to a dictionary of points
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        # At the end of this loop, 'points' dictionary will contain each unique number
        # from 'nums' as the key and the total sum of that number as the value.

        # Step 2: Sort the keys of the dictionary
        sorted_keys = sorted(points.keys())
        # This ensures that we process the numbers in ascending order.

        # Step 3: Dynamic Programming to decide whether to take or skip a number
        prev_key = None
        take, skip = 0, 0
        for key in sorted_keys:
            # If the current key is adjacent to the previous key (difference is 1)
            if prev_key is not None and key - prev_key == 1:
                # Decide between taking the current number or skipping it.
                take, skip = skip + points[key], max(take, skip)
            else:
                # If the current key is NOT adjacent to the previous key,
                # we can safely add the points of the current key to either 'take' or 'skip'.
                take, skip = max(take, skip) + points[key], max(take, skip)

            prev_key = key
        # The maximum of 'take' and 'skip' will give the maximum points we can earn.

        return max(take, skip)


'''
Runtime
Details
76ms
Beats 88.28%of users with Python3
Memory
Details
18.31MB
Beats 68.01%of users with Python3
'''
