'''
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []
 

Constraints:

0 <= turnedOn <= 10
'''


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        # Loop through all possible combinations of hours and minutes and count the number of set bits
        for h in range(12):
            for m in range(60):
                # Check if the number of set bits in hours and minutes equals the target number
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Add the valid combination of hours and minutes to the output list
                    output.append(f"{h}:{m:02d}")
        return output


'''
Runtime
37
ms
Beats
72.96%
of users with Python3
Memory
17.34
MB
Beats
12.81%
of users with Python3
'''
