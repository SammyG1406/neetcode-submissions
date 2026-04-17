class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array was initially sorted in ascending order
        # its been rotated for sure between 1 and n times
        # all elements in the rotated sorted array are unqiue
        # return the minimum element of the array
        # when the array is rotated, it moves to the right n number of times
        # we dont know how many times its been shifted
        # 

        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
            
            m = (left + right)//2
            res = min(res, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1

        return res