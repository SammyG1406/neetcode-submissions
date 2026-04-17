class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            complete=nums[i]
            if complete in hashmap:
                return True
            hashmap[nums[i]]=i
        return False