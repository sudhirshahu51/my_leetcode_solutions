#problem link https://leetcode.com/problems/pascals-triangle/
#Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]   
        else:
            i, pascal_tri = 2,[[1], [1,1]]
            while i < numRows:
                last_base = pascal_tri[-1] 
                new_base = []
                j = 1
                while j < (len(last_base)):   
                    new_base.append(last_base[j-1] + last_base[j])
                    j+=1
                new_base = [1] + new_base + [1]
                pascal_tri.append(new_base)
                i+=1
            return pascal_tri
        