#Happy_Number
class Solution:
    def isHappy(self, n: int) -> bool:
        results = []
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 1: return True
            elif n in results: return False
            else: results.append(n)