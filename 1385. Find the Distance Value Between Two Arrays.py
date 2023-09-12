'''
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
 

Constraints:

1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100
'''


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res, buckets = 0, dict()  # (minVa, maxVal)

        def getKey(val):
            return val // d

        def addVal(val):
            key = getKey(val)
            # save only min and max value in bucket, others values not
            if key in buckets:
                if buckets[key][0] > val:
                    buckets[key][0] = val
                elif buckets[key][1] < val:
                    buckets[key][1] = val
            else:
                buckets[key] = [val, val]

        # initialize buckets
        for val in arr2:
            addVal(val)

        for val in arr1:
            key = getKey(val)
            if key in buckets:
                continue  # in one bucket all values x < d
            # check sibling buckets
            if key - 1 in buckets and val - buckets[key-1][1] <= d:
                continue  # maxVal from the left side is nearest
            if key + 1 in buckets and buckets[key+1][0] - val <= d:
                continue  # minVal from the right side is nearest
            res += 1

        return res


'''
Runtime
Details
67ms
Beats 98.59%of users with Python3
Memory
Details
16.46MB
Beats 58.78%of users with Python3
'''
