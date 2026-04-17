class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = [0] * len(height)
        left = 0
        maximum = float("-inf")

        while left < len(height):
            if height[left] >= maximum:
                maximum = height[left]
                res[left] = 0
            else:
                res[left] = maximum - height[left]
            left += 1
        
        right = len(height) - 1
        maximum = float("-inf")

        while right > -1:
            if height[right] >= maximum:
                maximum = height[right]
                res[right] = 0
            else:
                res[right] = min(res[right],maximum - height[right])
            right -= 1

        return sum(res)