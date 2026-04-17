class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        width=len(matrix[0])-1


        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:  # Check if target is in this row
                row = mid
                break
            elif matrix[mid][0] > target:  # Target is above this row
                right = mid - 1
            else:  # Target is below this row
                left = mid + 1
        else:
            return False
        
        
        row=mid
        left=0
        while left <= width:
            middle=(left+width)//2
            if matrix[row][middle]==target:
                return True
            elif matrix[row][middle]<target:
                left=middle+1
            elif matrix[row][middle]>target:
                width=middle-1
        
        return False

        
            
        