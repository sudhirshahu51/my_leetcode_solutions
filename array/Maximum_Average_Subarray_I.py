#problem link https://leetcode.com/problems/maximum-average-subarray-i/submissions/
#Maximum Average Subarray I
class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum_4 = sum_win = sum(nums[:k])
        for i in range(len(nums) - k):n
            sum_win += nums[i+k] - nums[i]
            max_sum_4 = max(max_sum_4,sum_win)
        return max_sum_4/k
    