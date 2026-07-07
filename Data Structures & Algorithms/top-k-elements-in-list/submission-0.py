from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = Counter(nums)
        most_common = n_count.most_common(k)
        return [num for num,freq in most_common]