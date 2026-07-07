class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         has_map = {}
         for i,n in enumerate(nums):
            compliment = target-n
            if compliment in has_map:
                return [has_map[compliment],i]
            has_map[n]=i
