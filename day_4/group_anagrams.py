class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for i in strs:
            m = "".join(sorted(i))
            if m in grouped_anagrams:
                c = grouped_anagrams[m]
                c.append(i)
                grouped_anagrams[m] = c
            else:
                grouped_anagrams[m] = [i]
        grouped_anagrams = grouped_anagrams.values()
        return grouped_anagrams