class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left=1
        right=max(piles)

        res=right
        while left<=right:
            mid=((left+right)//2)
            hours=0
            for i in range(len(piles)):
                hours+=math.ceil(piles[i]/mid)

            if hours<=h:
                res=min(res,mid)
                right=mid-1
            else:
                left=mid+1
        
        return res
        
            

        