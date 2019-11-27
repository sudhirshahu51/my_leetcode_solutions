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



class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [[0 for _ in range(i+1)] for i in range(rowIndex+1)]
        
        def helper(i,j):
            if j==0 or j==i: return 1
            if res[i][j] == 0:
                res[i][j] = helper(i-1, j) + helper(i-1, j-1)
            return res[i][j]
        
        row = res[rowIndex]
        for j in range(rowIndex+1):
            row[j] = helper(rowIndex,j) 

        return res[rowIndex]