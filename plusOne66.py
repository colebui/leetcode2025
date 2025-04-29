class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        remainder = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += remainder
            if digits[i] < 10:
                remainder = 0
                break
            digits[i] = 0
        if remainder == 0:
            return digits
        else:
            return [1]+digits