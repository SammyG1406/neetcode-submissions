class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h cannot be less than the length of piles
        # piles is an unsorted array
        # only one pile can be finished an hour
        # the rate of k that will result in the
        # smallest number of hours will be the max of piles
        # we can start with that and then our lower bound
        # lower bound is what we are trying to optimise so we can go with 0.

        lower = 1
        right = max(piles)
        minimum = float('inf')
        while lower <= right:
            val = (lower + right)//2
            count = 0
            for n in piles:
                count += math.ceil(n/val)
            if count <= h:
                minimum = min(minimum, val)
                right = val - 1
            else:
                lower = val + 1
        
        return minimum
                    
