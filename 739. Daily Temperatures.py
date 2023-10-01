'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                res[st[-1]] = i-st[-1]
                st.pop()
            st.append(i)
        return res


'''
Runtime
Details
1068ms
Beats 55.26%of users with Python3
Memory
Details
30.79MB
Beats 62.41%of users with Python3
'''
