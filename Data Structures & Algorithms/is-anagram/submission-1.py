class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = sorted(s)
        l2 = sorted(t)
        if len(l1) == len(l2):
            if l1 == l2:
               return True
        return False
