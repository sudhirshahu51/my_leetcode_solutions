#problem link https://leetcode.com/problems/reshape-the-matrix/
#Reshape the Matrix

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums:
            if len(nums)*len(nums[0]) == r*c:#checking legal parameter
                flat_lis = [item for sublist in nums for item in sublist] #Flattening
                mat_nums = [flat_lis[row*c:(row +1)*c] for row in range(r)]
                return mat_nums
            else:
                return nums
        else:
            return nums