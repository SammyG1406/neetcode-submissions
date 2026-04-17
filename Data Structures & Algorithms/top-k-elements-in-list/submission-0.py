class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        print(hashmap)

        array=[]
        for i in range(k):
            max_key=max(hashmap, key=hashmap.get)
            array.append(max_key)
            hashmap.pop(max_key)
        
        return array