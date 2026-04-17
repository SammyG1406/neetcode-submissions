class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            
        for key in freq:
            store[freq[key]].append(key)
        print(store, freq)
        
        res = []
        for i in range(len(store) - 1, 0, -1):
            for num in store[i]:
                res.append(num)
                if len(res) == k:
                    return res