class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [height[0] for height in sorted(zip(names, heights), key = lambda h: -h[1])]