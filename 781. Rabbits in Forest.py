'''
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11
 

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000
'''


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = {}
        count = 0

        for answer in answers:
            if answer == 0:
                # This must be the only rabbit of its color.
                count += 1
            elif answer not in counts or counts[answer] == 0:
                # This is the first time the color appears.
                counts[answer] = 1
                # Add all rabbits having this new color.
                count += answer + 1
            else:
                # Add one to how many times answer occurred.
                counts[answer] += 1
                if counts[answer] > answer:
                    # If n+1 rabbits have said n,
                    # this color group is complete.
                    counts[answer] = 0

        return count


'''
Runtime
Details
39ms
Beats 96.62%of users with Python3
Memory
Details
16.11MB
Beats 99.60%of users with Python3
'''
