class Solution:
    def possibleStringCount(self, word: str) -> int:
        previousChar = ""
        sum = 1
        for char in word:
            if char == previousChar:
                sum += 1
            else:
                previousChar = char
        return sum