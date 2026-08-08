class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = best = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            best = max(best, i - start + 1)
            seen[c] = i
        return best