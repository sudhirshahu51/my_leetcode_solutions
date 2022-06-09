#Single_number 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Simple and easy to understand.
        return ((2 * sum(set(nums))) - sum(nums))