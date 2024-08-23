class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        for i in range(32):
            if (n >> i) & 1:
                ans += 1
        
        return ans