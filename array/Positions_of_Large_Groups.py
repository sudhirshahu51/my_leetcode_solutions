#link https://leetcode.com/problems/positions-of-large-groups/
#830. Positions of Large Groups

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """ """
        out = []
        i =0
        while i < (len(S) -1):
            j = i
            while j < (len(S) -1) and S[j] == S[j+1]:
                j += 1
            if (j - i + 1) >= 3: #Checking condition for length.  
                out.append([i,j])
            i = j
            i+=1
        return out