
#problem link https://leetcode.com/problems/house-robber/
#House Robber


class Solution:
    def rob(self, nums: List[int]) -> int:
        odd = even = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                odd = max(even, odd + nums[i])
            else:
                even = max(odd, even + nums[i])
        return max(odd, even)
    
    
    
    
