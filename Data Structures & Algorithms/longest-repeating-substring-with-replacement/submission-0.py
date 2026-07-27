import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time complexity O(26*n)
        longest_substring = 0
        # alphabet_dict = dict.fromkeys(string.ascii_uppercase, 0) 
        alphabet_dict = {}
        l=0
        for r in range(len(s)):
            # condition is most frequent letter - length or vica versa <= K 
                alphabet_dict[s[r]] = 1+alphabet_dict.get(s[r],0)
                # edge case in case it has numbers or special characters in input
                while (r-l+1) - max(alphabet_dict.values()) > k:
                       alphabet_dict[s[l]] -=1
                       l+=1
                 
                longest_substring = max(longest_substring,r-l+1)
        return longest_substring
      