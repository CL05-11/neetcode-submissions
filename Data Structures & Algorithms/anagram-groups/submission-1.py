from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        GAL_dict = {}
        for n in strs:
            key = tuple(sorted(n))
            if key in GAL_dict:
                GAL_dict[key]+=[n]
            else:
                GAL_dict[key]=[n]
        return list(GAL_dict.values())