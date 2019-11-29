#problem link https://leetcode.com/problems/pascals-triangle-ii/
#Pascal's triangle II.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1] 
        elif rowIndex == 1: return [1,1]
        else:
            i, last_base = 1,[1,1]
            while i < rowIndex:
                add_base_ele = []
                j = 1
                while j < (len(last_base)):   
                    add_base_ele.append(last_base[j-1] + last_base[j])
                    j+=1
                last_base = [1] + add_base_ele + [1]
                i+=1
                if i == rowIndex: break   
            return last_base  



