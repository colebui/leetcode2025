class Solution:
    def climbStairs(self, n: int, hashmap = {}) -> int:
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        if (n in hashmap):
            return hashmap[n]
        hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return hashmap[n]
        