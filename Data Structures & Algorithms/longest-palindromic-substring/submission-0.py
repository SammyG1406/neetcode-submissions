class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        idx = 0
        string = []
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1 > length):
                    idx = l
                    length = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1 > length):
                    idx = l
                    length = r - l + 1
                l -= 1
                r += 1
        return s[idx : idx + length]