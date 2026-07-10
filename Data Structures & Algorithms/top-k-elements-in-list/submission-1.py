class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         count = {}
         n_count = [[] for i in range(len(nums)+1)]

         for num in nums:
            count[num] = 1+count.get(num,0)
         
         for n,c in count.items():
            n_count[c].append(n)
        
         res = []
         for i in range(len(n_count)-1,0,-1):
           for num in n_count[i]:
            res.append(num)
            if len(res) == k:
                return res