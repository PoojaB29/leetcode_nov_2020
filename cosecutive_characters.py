##Leetcode November 2020
#Day 3: Consecutive characters
#Input: s = "leetcode"
#Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

#Return the power of the string.
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.


class Solution:
    def maxPower(self, s: str) -> int:
        count, max_count = 1,1
        prev = s[0]
        for i in range(1,len(s)):
            if s[i] == prev:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
                prev = s[i]
        return max_count