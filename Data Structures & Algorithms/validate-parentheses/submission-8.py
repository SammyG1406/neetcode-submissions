class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'[' : ']', '(' : ')', '{' : '}'}
        stack = []
        
        index = 0
        while index < len(s):
            if s[index] in hashmap:
                stack.append(s[index])
            else:
                if not stack or hashmap[stack.pop()] != s[index]:
                    return False
            index += 1
        return not stack