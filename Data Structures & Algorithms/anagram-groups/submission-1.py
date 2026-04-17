class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return False
        
        hashmap = {}

        for i in range(len(strs)):
            array = [0] * 26
            for j in range(len(strs[i])):
                strng = strs[i]
                val = ord(strng[j]) - ord('a')
                array[val] += 1
            
            key = tuple(array)
            
            if key in hashmap:
                hashmap[key].append(strs[i])
            else:
                hashmap[key] = [strs[i]]
        
        return list(hashmap.values())
        
        