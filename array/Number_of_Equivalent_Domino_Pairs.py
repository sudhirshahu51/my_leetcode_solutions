#Number of Equivalent Domino Pairs
#https://leetcode.com/problems/number-of-equivalent-domino-pairs/
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import Counter
        sorted_domi = [sorted(i) for i in dominoes]
        count_dict = {}
        for lis in sorted_domi:count_dict[str(lis)] = count_dict.get(str(lis),0) + 1
        count = 0
        for k,v in count_dict.items():
            count+= ((v*(v-1))/2)
        return int(count)
