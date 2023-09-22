'''
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
 

Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
'''


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(len(sequence)//len(word)+1, 0, -1):
            if i*word in sequence:
                return i
        else:
            return 0


'''
Runtime
Details
46ms
Beats 12.97%of users with Python3
Memory
Details
15.96MB
Beats 100.00%of users with Python3
'''
