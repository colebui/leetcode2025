class Solution:
    def triangleType(self, nums: List[int]) -> str:
        print(*nums)
        if not self.is_valid_triangle(*nums):
            return "none"
        mySet = set()
        for num in nums:
            mySet.add(num)
        if len(mySet) == 1:
            return "equilateral"
        if len(mySet) == 2:
            return "isosceles"
        return "scalene"

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def triangleType2(self, nums: List[int]) -> str:
        a, b, c = nums
        if not self.is_valid_triangle(a, b, c):
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "scalene"