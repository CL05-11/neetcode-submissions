class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input  - an array & output - array of indices
        # solution - O(n)
        my_dict = {}
        for i,j in enumerate(nums):
            # its printing i = key and j = value(list)
            compute = target - j
            if compute in my_dict:
                return[my_dict[compute],i]
            my_dict[j] = i
        