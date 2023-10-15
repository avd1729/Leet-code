'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''


class Solution:
    # Binary Search Approach
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)

        def ok(k):
            # the idea is to use binary search to find the length `k`
            # then we check if there is any nums1[i : i + k] == nums2[i : i + k]
            s = set(tuple(nums1[i: i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i: i + k]) in s for i in range(M - k + 1))

        # init possible boundary
        l, r = 0, min(N, M)
        while l < r:
            # get the middle one
            # for even number of elements, take the upper one
            m = (l + r + 1) // 2
            if ok(m):
                # include m
                l = m
            else:
                # exclude m
                r = m - 1
        return l


'''
Runtime
Details
274ms
Beats 91.84%of users with Python3
Memory
Details
19.02MB
Beats 81.57%of users with Python3
'''
