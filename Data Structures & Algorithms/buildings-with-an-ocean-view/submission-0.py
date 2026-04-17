class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        array = []
        res[len(heights) - 1] = 1
        current_max = heights[-1]
        for i in range(len(heights) -2, -1, -1):
            if heights[i] > current_max:
                res[i] = 1
                current_max = heights[i]
        
        for i in range(len(heights)):
            if res[i] == 1:
                array.append(i)
        
        return array