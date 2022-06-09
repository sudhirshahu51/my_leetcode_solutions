#Third_Maximum_Number
#link- https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Use sorted array index using len condition.
           """
        set_nums = set(nums)
        if len(set_nums) <=2: return sorted(set_nums)[-1]
        else: return sorted(set_nums)[-3]   