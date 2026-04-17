class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            over = target - nums[i]
            if over in hashmap:
                return [hashmap[over], i]
            hashmap[nums[i]] = i
        
        

        