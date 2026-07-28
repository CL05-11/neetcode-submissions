class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # O(n^2) and space O(n)
        results = [0] * len(temperatures)
        count = 0

        for i, n in enumerate(temperatures):
           for k in range(i+1,len(temperatures)):
             if temperatures[k] > temperatures[i]:
                results[i] = k-i
                break
    
        return results

