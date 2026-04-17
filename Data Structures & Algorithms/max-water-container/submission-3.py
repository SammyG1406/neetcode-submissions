class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maximum = float("-inf")

        while left <= right:
            store = min(heights[left], heights[right]) * (right-left)
            maximum = max(store, maximum)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return maximum