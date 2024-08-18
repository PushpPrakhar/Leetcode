class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        ls = zip(profits, capital)
        ls.sort(key=lambda x: x[1])
        import heapq
        heap = []
        count = 0
        i = 0
        while count < k:
            while i < len(ls) and ls[i][1] <= w:
                heapq.heappush(heap, -ls[i][0])
                i += 1

            if heap:
                w += -heapq.heappop(heap)
                count += 1
            else:
                break
        return w