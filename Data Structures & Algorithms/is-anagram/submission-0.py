class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check for None values
        if s is None or t is None:
            return False
        
        # If lengths are not equal, return False immediately
        if len(s) != len(t):
            return False
        
        # Create hashmaps to count character occurrences
        hashmap1 = {}
        hashmap2 = {}

        # Count characters for string s
        for letter in s:
            hashmap1[letter] = hashmap1.get(letter, 0) + 1

        # Count characters for string t
        for letter in t:
            hashmap2[letter] = hashmap2.get(letter, 0) + 1

        # Print hashmaps (for debugging purposes)
        print("Hashmap 1:", hashmap1)
        print("Hashmap 2:", hashmap2)

        # Compare hashmaps
        return hashmap1 == hashmap2

        
        

        
        