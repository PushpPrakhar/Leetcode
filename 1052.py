class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        satisfied = sum(c for i,c in enumerate(customers) if grumpy[i] == 0)
        madeSatisfied = 0
        windowSatisfied = 0

        for i, customer in enumerate(customers):
            if grumpy[i] == 1:
                windowSatisfied += customer
            if i >= minutes and grumpy[i - minutes] == 1:
                windowSatisfied -= customers[i - minutes]
            madeSatisfied = max(madeSatisfied, windowSatisfied)
                
        return satisfied + madeSatisfied
            