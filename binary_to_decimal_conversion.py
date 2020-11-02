#Leetcode November 2020
#Day 1: Convert binary number in a linked list to integer
#Input: head = [1,0,1]
#Output: 5
#Explanation: (101) in base 2 = (5) in base 10




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        while head:
            res += str(head.val)
            head = head.next
        return int(res,2)
            