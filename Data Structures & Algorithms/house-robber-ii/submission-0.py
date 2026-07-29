class Solution:
    def rob(self, nums: List[int]) -> int:
       
        if len(nums) == 1:
            return nums[0]
        # this hsows the case that including first and then including last element
        return max(self.high_rob (nums[1:]), self.high_rob (nums[:-1]))
        
    def high_rob(self, nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
        
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            # since first and last element are adjacent we cannot add them so we start from index 1
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],nums[i]+dp[i-2])
            return dp[-1]