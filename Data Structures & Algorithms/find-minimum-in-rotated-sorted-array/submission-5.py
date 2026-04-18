class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given an array of length n and its initially sorted in ascending order.
        # it has been rotated between 1 and n times
        # output is the minimum value in the sorted array
        # minimum should ideally be at the left most pointer
        # since it was iniitally soted and we have to find a target value thats minimum,
        # it sounds like a problem for a tree or binary search
        # if right cross L or is equal to it, we know we have arrived at the smallest element
        # if we arrive at a mid value thats higher than left 
        # [5,4,0,1,2,3]
        # we know that the number is either at the start osomwehere in between
        # if its rotated between 1..n-1 times, the left will be greater than the right
        # if the element in the middle is greater than the left, it is rotated

        L = 0
        R = len(nums) - 1 
        M = (L + R)//2
        while L < R:
            if nums[L] < nums[R]:
                return nums[L]
            if nums[M] < nums[R]:
                R = M
            else:
                L = M + 1
            M = (L + R)//2    
        return nums[L]
            
            

        