class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Use integer division to calculate the midpoint
            print(left, mid, right)  # Debug statement to track the search range

            if nums[mid] == target:
                return mid  # Return the index if the target is found
            elif target < nums[mid]:
                right = mid - 1  # Narrow down to the left half
            else:
                left = mid + 1  # Narrow down to the right half

        return -1
    
        