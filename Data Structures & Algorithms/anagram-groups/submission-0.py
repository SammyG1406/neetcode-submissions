class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return False
        
        hashmap={}

        for word in strs:
            alphabets=[0]*26
            for i in range(len(word)):
                alphabets[ord(word[i])-ord('a')] +=1
            
            key = tuple(alphabets)

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]

        return list(hashmap.values())