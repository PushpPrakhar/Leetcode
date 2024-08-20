class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ans = 0
        i = 0
        miss = 1

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                ans +=1
        
        return ans
