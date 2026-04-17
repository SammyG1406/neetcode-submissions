class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         
        initial_sums=[0]*len(nums)
        
        for i in range(len(nums)):
            initial_sums[i]=0-nums[i]
        
        array=set()
        for i in range(len(initial_sums)):
            target=initial_sums[i]
            hashmap={}
            for j in range(len(nums)):
                if j!=i:
                    current=target-nums[j]
                    if current in hashmap:
                        triplet = tuple(sorted((nums[i], nums[j], current)))
                        array.add(triplet)
                    else:
                        hashmap[nums[j]]=current
        
        return[list(triplet) for triplet in array]


