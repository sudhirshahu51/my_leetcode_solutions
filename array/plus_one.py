#problem link https://leetcode.com/problems/plus-one/
#Binary search

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = "".join(map(str, digits))
        incr_a = int(a) + 1
        return list(str(incr_a))