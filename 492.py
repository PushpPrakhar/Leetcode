class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(math.sqrt(area))
        res = [area,1]
        while W >= 1:
            if area % W == 0:
                res = [int(area/W),W]
                break
            W -= 1
        return res
