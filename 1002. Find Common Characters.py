'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        from typing import List

        # Initialize a Counter object with the characters of the first word
        common = Counter(words[0])

        # Iterate over the remaining words and update the common Counter object
        for word in words[1:]:
            # Initialize a Counter object for the current word
            word_count = Counter(word)
            # Update the common Counter object to only include characters present in both
            common &= word_count

        # Convert the common Counter object to a list of characters
        result = []
        for char, count in common.items():
            result += [char] * count

        return result


'''
Runtime
Details
45ms
Beats 94.91%of users with Python3
Memory
Details
16.44MB
Beats 44.30%of users with Python3
'''
