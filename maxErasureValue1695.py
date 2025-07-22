class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        highestSum = 0
        currentSum = 0
        left = 0
        right = 0
        seen = set()
        while (right < len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currentSum -= nums[left]
                left += 1
            seen.add(nums[right])
            currentSum += nums[right]
            highestSum = max(highestSum, currentSum)
            right += 1
        return highestSum
