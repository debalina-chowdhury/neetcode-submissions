from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = dict(Counter(nums))
        dict2 = dict(sorted(dict1.items(), key = lambda item: item[1])[::-1])
        return list(dict2.keys())[:k]