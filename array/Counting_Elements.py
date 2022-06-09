#Counting_Elements
class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter
        count_dict = Counter(arr)      
        count = sum([v for x,v in count_dict.items() if count_dict.get(x+1, 0)])
        return count