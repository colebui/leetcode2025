class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        print(t)
        print(t[1:-1])
        if s in t[1:-1]:
            return True
        return False