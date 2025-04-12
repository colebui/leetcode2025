# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the current pointers for both lists and the carry digit
        current1 = l1
        current2 = l2
        carryDigit = 0
        head = ListNode(0)  # Dummy node to start the result list
        currentResult = head

        while current1 or current2 or carryDigit:
            # Get the current values, treating None as 0
            value1 = current1.val if current1 else 0
            value2 = current2.val if current2 else 0
            
            # Calculate the sum including the carry digit
            value = value1 + value2 + carryDigit
            valueFirstDigit = value % 10  # The digit for the current place
            carryDigit = value // 10  # The carry for the next place
            
            # Add the calculated digit to the result list
            currentResult.next = ListNode(valueFirstDigit)
            currentResult = currentResult.next

            # Move to the next nodes in both lists if they exist
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next

        return head.next  # Return the next of the dummy node (actual result list)