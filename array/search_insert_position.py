#problem link https://leetcode.com/problems/search-insert-position/
#Binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums:
            if target in nums:
                return int(nums.index(target))
            elif nums[(len(nums) -1)] < target:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if target < nums[i]:
                        return i
        else: return 0