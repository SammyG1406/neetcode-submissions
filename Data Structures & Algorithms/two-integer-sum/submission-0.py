class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums is None:
            return False
        
        hashmap={}
        for i in range(len(nums)):
            summer=target-nums[i]
            if summer in hashmap:
                return [hashmap[summer],i]
            hashmap[nums[i]]=i
        
        

        