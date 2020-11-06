#Leetcode November 2020
#Day 5: Minimum cost to move chips to the same position
#Input: position = [1,2,3]
#Output: 1
#Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
#Second step: Move the chip at position 2 to position 1 with cost = 1.
#Total cost is 1.

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0 , 0
        for i in position:
            if i%2==0:
                even+=1
            else:
                odd+=1
        if even == len(position) or odd == len(position):
            return 0
        return min(even, odd)
            