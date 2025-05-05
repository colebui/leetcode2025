class Solution:
    def isHappy(self, n: int) -> bool:
        
        my_set = set()

        while (n > 1):
            sum = 0
            for digit in str(n):
                sum += int(digit)*int(digit)
            n = sum
            if n in my_set:
                return False
            my_set.add(n)
            

        return True