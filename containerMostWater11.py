class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxA = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            length = right - left
            tmpHeight = min(height[left], height[right])
            maxA = max(maxA, length * tmpHeight)
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxA
 