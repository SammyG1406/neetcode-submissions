class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []
        temp = []
        space = 0
        num = 0
        total = 0
    
        for word in words:
            print(word)
            if len(word) + len(temp) + total <= maxWidth:
                temp.append(word)
                total += len(word)
            else:
                store = ""
                if len(temp) == 1:
                    store += temp[0]
                    store += " " * (maxWidth - total)
                else:
                    set_space = (maxWidth - total)//(len(temp) - 1)
                    modulo = (maxWidth - total)%(len(temp) - 1)
                    for d in range(len(temp) - 1):
                        store += temp[d]
                        store += " " * (set_space + (1 if d < modulo else 0))
                    store += temp[-1]
                res.append(store)
                temp = [word]
                total = len(word)
        
        last = " ".join(temp)
        last += " " * (maxWidth - len(last))
        res.append(last)

        return res
                    
                    


        