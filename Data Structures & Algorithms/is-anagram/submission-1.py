class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # an anagram will make sure to have the same number
        # of each letter. If it doesn, your return the anagram
        # first take each word and then use a hashmap to increment the frequency of each letter
        
        if len(s) != len(t):
            return False
        hashs = defaultdict(int)
        hasht = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in hashs:
                hashs[s[i]] = 1
            else:
                hashs[s[i]] +=1
            if t[i] not in hasht:
                hasht[t[i]] = 1
            else:
                hasht[t[i]] +=1
        
        for i in range(len(s)):
            if hashs[s[i]] != hasht[s[i]]:
                return False
        return True
        