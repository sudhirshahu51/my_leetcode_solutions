#problem link https://leetcode.com/problems/find-pivot-index/
#Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Easy to understand """
        
        piv = -1
        sum_after_i= sum(nums)
        sum_before_i = 0
        if len(nums) not in [0,1]:
            for i in range(len(nums)):
                sum_after_i -=nums[i] #sum of numbers after i'th iteration
                if sum_before_i == sum_after_i:
                    piv = i
                    break 
                sum_before_i += nums[i] ##sum of numbers till i'th iteration(for i+1 )
            return piv 
        else:return piv

        
