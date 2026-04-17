class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maximum = float('-inf')
        while left <= right :
            total = min(heights[left], heights[right]) * (right - left)
            if total > maximum:
                maximum = total
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
            
        return maximum