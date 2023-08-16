'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''


class Solution(object):
    def generate(self, numRows):
        # Create an array list to store the output result...
        output = []
        for i in range(numRows):
            if (i == 0):
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                # Calculate for each of the next values...
                while (j < i):
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j-1] + prev[j])
                    j += 1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output       # Return the output list of pascal values...

# 41ms runtime 16.40mb memory
