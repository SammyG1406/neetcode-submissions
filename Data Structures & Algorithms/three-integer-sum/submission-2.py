class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Return three indicies of the numbers whose sum adds up to
        # 0. No duplicate triplets so better to
        # group the result in a set
        # Complexity is O(n^2) and O(1) space complexity
        # So use only the array
        # The array is unsorted
        # at any number, it's opposite being added to it will
        # return to 0
        # no duplicates of the array can be made
        # if we sorted the array this would allow for 

        nums.sort()
        result = set()
        for i in range(len(nums)):
            store = 0 - nums[i]
            index = i
            left = 0 
            right = len(nums) - 1
            while left < right:
                if left == index:
                    left += 1
                elif right == index:
                    right -= 1
                total = nums[left] + nums[right]
                if left != right:
                    if  total == store:
                        holder = tuple(sorted((nums[left], nums[index], nums[right])))
                        if holder not in result:
                            result.add(holder)
                        left += 1
                        right -= 1
                    elif total < store:
                        left += 1
                    else:
                        right -= 1
        return list(result)