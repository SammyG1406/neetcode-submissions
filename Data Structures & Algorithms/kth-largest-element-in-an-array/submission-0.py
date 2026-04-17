

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        
        i = 1
        length = len(nums) - 1

        while i != k:
            i += 1
            length -= 1
        return nums[length]


        