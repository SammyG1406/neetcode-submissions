class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        inverses = []
        for num in nums:
            inverses.append(0 - num)
        res = set()
        for i in range(len(inverses)):
            target = inverses[i]
            store = {}
            for k in range(len(nums)):
                if k != i:
                    if target - nums[k] in store:
                        temp = [nums[k], target - nums[k], nums[i]]
                        temp.sort()
                        res.add(tuple(temp))       
                    else:
                        store[nums[k]] = k
        return list(res)