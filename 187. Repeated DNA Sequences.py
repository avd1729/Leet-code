'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        # step 1:
        if n <= 10:
            return []
        # step 2:
        d = dict()
        for i in range(n-9):
            key = s[i:i+10]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
        # step 3:
        return [key for key in d.keys() if d[key] > 1]


'''
Runtime
Details
53ms
Beats 93.10%of users with Python3
Memory
Details
30.20MB
Beats 5.73%of users with Python3
'''
