#link- https://leetcode.com/problems/find-common-characters/
#Find Common Characters

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter, defaultdict 
        output = []
        initial_chars= Counter(A[0])
        
        count_dict =  defaultdict(list)
        for key, val  in initial_chars.items():count_dict[key].append(val)
        del initial_chars
        
        for strr in A[1:]:
            counts = Counter(strr)
            count_dict_keys = list(count_dict.keys())
            for key in count_dict_keys:
                if key not in counts.keys(): del count_dict[key]
                else: count_dict[key].append(counts[key])
                    
        #Character counts
        min_dict = {k:min(val) for k,val in count_dict.items()} 
        for k,v in min_dict.items():
            output +=  [k]*v
        return output
