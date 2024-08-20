class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = int(sqrt(c))

        while l<=r:
            sum = l*l + r * r
            if sum == c:
                return True
            elif sum < c:
                l +=1
            else:
                r-= 1
        return False