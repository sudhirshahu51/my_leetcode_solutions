# Group_Anagrams



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        if strs:
            for i in strs:
                srt_str = "".join(sorted(i))
                if anagrams.get(srt_str,0): anagrams[srt_str].append(i)
                else: anagrams[srt_str] = [i]  

        return anagrams.values()


