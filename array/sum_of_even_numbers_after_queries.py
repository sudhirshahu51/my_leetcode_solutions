class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        """ even number use some of even numbers then use the the changed if even have it else remove .
        
        
        """
        ##Try to write full code again.
        sum_even = sum([n for n in A if n%2 ==0])
        out = []
        for q in queries:
            if A[q[1]] %2==0:
                sum_even -= A[q[1]]
            A[q[1]] += q[0]
            if A[q[1]] %2==0:
                sum_even += A[q[1]]
                out.append(sum_even)
            else:
                out.append(sum_even)

        return out
        
        
        
        