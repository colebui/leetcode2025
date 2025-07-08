class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}

        if len(s) != len(t):
            return False
        for char in s:
            myDict[char] = myDict.get(char, 0) + 1
        for char in t:
            if char not in myDict:
                return False
            myDict[char] -= 1
            if myDict[char] < 0:
                return False
        return True
