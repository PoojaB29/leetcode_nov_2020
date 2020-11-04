#Leetcode November 2020
#Day 2: Insertion Sort List
#Input: 4->2->1->3
#Output: 1->2->3->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sorted = None
        current = head
        while current!= None:
            next = current.next
            sorted = self.sortedInsert(sorted, current)
            current = next
        head = sorted
        return head
         
    def sortedInsert(self, head, new_node):
        current = None
        if head == None or head.val >= new_node.val:
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next !=None and current.next.val < new_node.val:
                current = current.next
            new_node.next =current.next
            current.next = new_node
        return head
                
