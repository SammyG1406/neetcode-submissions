class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        print(hashmap)
        string = ""
        for char in order:
            if char in hashmap:
                string += char * hashmap[char]
                hashmap[char] = 0
        
        for val in hashmap:
            if hashmap[val] != 0:
                string += val * hashmap[val]
        
        return string
        

