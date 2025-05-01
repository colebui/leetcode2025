class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        candidate = nums[0]
        count = 0
        for number in nums:
            if number == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = number
                    count = 1
        return candidate
