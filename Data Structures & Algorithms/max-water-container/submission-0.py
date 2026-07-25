class Solution:
    def maxArea(self, heights: List[int]) -> int:
     max_res = 0

     l = 0
     r = len(heights)-1

     while l < r:
        height = min(heights[l],heights[r])
        width = r-l
        max_area = height * width
        
        if heights[l] < heights [r]:
            l+=1
        elif heights[r] < heights[l]:
            r-=1
        else:
             l+=1
             r-=1
        
        max_res = max(max_res,max_area)
     return max_res
        