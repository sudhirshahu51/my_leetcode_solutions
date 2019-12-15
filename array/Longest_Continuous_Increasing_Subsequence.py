#problem link https://leetcode.com/problems/longest-continuous-increasing-subsequence/
#Longest Continuous Increasing Subsequence
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest_arr = 0
        count, j = 0, 0
        if not nums:return 0
        while j < len(nums):
            if j < (len(nums) -1) and nums[j] < nums[j+1]:
                j+=1
                count+=1
            else:
                if count > longest_arr:
                    longest_arr = count
                j+=1
                count = 0
        return longest_arr + 1