#problem link https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_list = list(set(nums))  # Get set
        return True if len(set_list) < len(nums) else False  # check length

print("D", end = " ")
print("A", end = " ")