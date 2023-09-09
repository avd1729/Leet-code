'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        st = ""
        for i in address:
            if i == ".":
                st += '['+'.'+']'
            else:
                st += i
        return st


'''
Runtime
Details
32ms
Beats 91.63%of users with Python3
Memory
Details
16.18MB
Beats 84.49%of users with Python3
'''
