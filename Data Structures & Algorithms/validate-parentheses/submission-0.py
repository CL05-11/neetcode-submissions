class Solution:
    def isValid(self, s: str) -> bool:
     stack = []
     map_OC = {
        "}":"{",
        "]":"[",
        ")":"("
     }   
     for st in s:
        if st in map_OC:
            if stack and stack[-1] == map_OC[st]:
               stack.pop()
            else:
                return False
        else:
            stack.append(st)

     return True if not stack else False
        

        

