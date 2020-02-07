
#Link https://leetcode.com/problems/monotonic-array/
#Monotonic Array


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        incre_monotone = None
        last_monotone = None
        out = True
        for i in range(len(A) -1):
            if A[i] == A[i+1]:continue
			elif  A[i] < A[i+1]:incre_monotone = True
            elif A[i] > A[i+1]:incre_monotone = False
           
                
            if last_monotone == None:last_monotone = incre_monotone
            elif last_monotone == incre_monotone:continue
            elif last_monotone != incre_monotone: 
                out = False
                break 
                
        return out
                