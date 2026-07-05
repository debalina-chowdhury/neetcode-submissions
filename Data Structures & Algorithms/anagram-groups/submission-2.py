from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        values = ()
        for s in strs:
            key = "".join(sorted(s))
            sorted_strs[key].append(s)
        return list(sorted_strs.values())