from typing import List
import collections

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_count = collections.Counter(digits)
        result = []

        # Check all 3-digit even numbers from 100 to 998
        for num in range(100, 1000, 2):  # step by 2 to ensure even numbers
            num_digits = [int(d) for d in str(num)]
            num_counter = collections.Counter(num_digits)
            
            if all(digit_count[d] >= num_counter[d] for d in num_counter):
                result.append(num)

        return result