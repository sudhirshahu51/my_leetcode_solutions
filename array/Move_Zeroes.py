#problem link https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] =[i for i in nums if i != 0] + [i for i in nums if i == 0]
        return nums