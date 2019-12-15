#problem link https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums) + 1)) - set(nums))

