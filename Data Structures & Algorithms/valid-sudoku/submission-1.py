class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                if board[i][j] != ".":

                    number = int(board[i][j])

                    boxIndex = (i//3) * 3 + j//3

                    if(number in rows[i] or 
                        number in cols[j] or 
                        number in boxes[boxIndex]):
                        return False
                    
                    rows[i].add(number)
                    cols[j].add(number)
                    boxes[boxIndex].add(number)
        return True
        
