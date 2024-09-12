class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = 0
        secondmx = 0

        for i, num in enumerate(nums):
            if num > mx:
                secondmx = mx
                mx = num
                ans = i
            elif num > secondmx:
                secondmx = num
        
        return ans if mx >= secondmx *2 else -1