class Solution:
    def isValid(self, s: str) -> bool:
        
        if s is None or (len(s)<2):
            return False
        
        array=[]
        opening_characters=['[','(','{']
        closing_characters=[']',')','}']
        k=0
    
        for i in range(len(s)):
            if (len(array)==0) and (s[i] in closing_characters):
                return False
            if s[i] in opening_characters:
                array.append(s[i])
                k+=1
            elif s[i] in closing_characters:
                character=array.pop()
                if character=="[" and s[i]!="]":
                    return False
                if character=="(" and s[i]!=")":
                    return False
                if character=="{" and s[i]!="}":
                    return False
                k-=1
        
        if k==0:
            return True
        return False
    
        



    