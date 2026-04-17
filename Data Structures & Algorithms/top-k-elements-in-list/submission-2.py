class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
        for key in freq:
            store[freq[key]].append(key)
        print(store, freq)
        
        res = []
        for i in range(len(store) - 1, -1, -1):
            print("here")
            for val in store[i]:
                if len(res) != k:
                    res.append(val)
                else:
                    return res
        return res
        