class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxM = 0
        hashMap = {}

        for R in range(len(s)):
            if s[R] in hashMap:
                hashMap[s[R]] += 1
            else:
                hashMap[s[R]] = 1
            vals = hashMap.values()
            while sum(vals) - max(vals) > k:
                hashMap[s[L]] -= 1
                vals = hashMap.values()
                L += 1
            maxM = max(maxM, (R-L) + 1)
        
        return maxM