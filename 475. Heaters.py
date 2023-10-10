'''
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3
 

Constraints:

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
'''


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort the houses and heaters
        houses.sort()
        heaters.sort()

        # Initialize the result to 0
        result = 0

        # For each house, find the closest heater to the left and the right
        for house in houses:
            left = bisect.bisect_right(heaters, house) - 1
            right = bisect.bisect_left(heaters, house)

            # If the house is to the left of all heaters, use the closest heater to the left
            if left < 0:
                result = max(result, heaters[0] - house)
            # If the house is to the right of all heaters, use the closest heater to the right
            elif right >= len(heaters):
                result = max(result, house - heaters[-1])
            # If the house is between two heaters, use the closer of the two
            else:
                result = max(result, min(
                    house - heaters[left], heaters[right] - house))

        # Return the result
        return result


'''
Runtime
Details
249ms
Beats 56.98%of users with Python3
Memory
Details
19.96MB
Beats 96.72%of users with Python3
'''
