#O(n) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        i = 0
        while (i < len(nums)):
            compliment = target - nums[i]
            if (compliment in hashmap):
                return [hashmap[compliment], i]
            else:
                hashmap[nums[i]] = i
                i += 1

#O(n^2) time complexity

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
#         i = 0
#         while (i < len(nums)):
#             j=i+1
#             while (j < len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     return [i,j]
#                 else:
#                     j += 1
#             i += 1