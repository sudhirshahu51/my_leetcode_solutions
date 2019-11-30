class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actual_rotate = k % len(nums)
        nums[:] = nums[-actual_rotate:]+ nums[:-actual_rotate]
