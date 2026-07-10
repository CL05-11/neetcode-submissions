class Solution:

    def encode(self, strs: List[str]) -> str:
         strsl = ""
         for n in strs:
            strsl = strsl+str(len(n))+"#"+n
         return strsl

    def decode(self, s: str) -> List[str]:
        strsl = []
        i = 0
        while i < len(s):
            j = i # here j = 0
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) 
            strsl.append(s[j+1:j+1+length]  )
            i=j+1+length
        return strsl

                   