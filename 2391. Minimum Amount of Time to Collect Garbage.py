'''
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
'''


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_minutes = 0  # Total minutes needed for garbage collection
        current_travel_time = 0  # Current travel time

        # Add the initial minutes required to collect garbage at the first house
        total_minutes += len(garbage[0])

        # Keep track of the last occurrence of each type of garbage
        last_garbage_indices = [-1, -1, -1]

        # Iterate through each house starting from the second house
        for house_index in range(1, len(garbage)):
            # Add the minutes required to collect garbage at the current house
            total_minutes += len(garbage[house_index])

            # Update the indices of the last occurrence of each type of garbage
            if "M" in garbage[house_index]:
                last_garbage_indices[0] = house_index - 1
            if "P" in garbage[house_index]:
                last_garbage_indices[1] = house_index - 1
            if "G" in garbage[house_index]:
                last_garbage_indices[2] = house_index - 1

        # Iterate through each travel segment
        for travel_index in range(len(travel)):
            # Add the current travel time
            current_travel_time += travel[travel_index]

            # Add the minutes required to collect garbage if a garbage truck is at the corresponding house
            for truck_index in range(3):
                if last_garbage_indices[truck_index] == travel_index:
                    total_minutes += current_travel_time

        return total_minutes


'''
Runtime
891
ms
Beats
63.63%
of users with Python3
Memory
39.28
MB
Beats
61.98%
of users with Python3
'''
