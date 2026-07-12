class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums: # if a number is 4 and (n-1 =  4-1=3 in numset then it will go to next number)
           if (num - 1) not in numset:
               length = 1
               while(num+length) in numset:
                     length+=1
               longest = max(longest,length)
        return longest


   
