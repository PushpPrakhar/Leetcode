class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= (n-1)*2
        if time < n:
            return 1 + time
        return n - (time - (n-1))