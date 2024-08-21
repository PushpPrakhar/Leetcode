class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        l=1 # minimum distance between two balls can be 1
        r = position[-1] - position[0] # distance between the first ans last position aka largest distance

        def numballs(force):
            balls = 0
            prevPosition = -force
            for pos in position:
                if pos - prevPosition >= force:
                    balls += 1
                    prevPosition = pos
            return balls
        
        while l < r:
            mid = r - (r-l)//2
            if numballs(mid) >=m:
                l = mid
            else:
                r = mid - 1
        
        return l
