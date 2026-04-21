class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the length of the longest consecutive sequence of elements that can be forrmed
        # The array is unsorted
        # the sequence is always moving ahead.
        # we can increment one to a sequence if we see that the number before it exists,
        # for element a, we need to set its sequence value to 1 + the number before it, if it exists
        # and for the same element a, if we find an element b thats greater than it
        # we set b's value to greater
        # can store these values a dictionary then return the max of the dictionary
        # conditions:
        # duplicates count
        # if lets say we find an element
        # we need to insert it. If it already exists then we increment it.
        # if it doesnt, we insert it and set its value to 1 + the previous of
        # its value, if it exists and then if its next value exists, we update the next's value to the current + 1
        # the start of a sequence does not have a left neighbour

        numSet = set(nums)
        maxValue = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                longest = 0
                while nums[i] + longest in numSet:
                    longest += 1
                maxValue = max(longest, maxValue)
        return maxValue