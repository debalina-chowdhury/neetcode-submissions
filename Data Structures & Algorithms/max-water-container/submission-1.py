class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights) - 1
        best = 0
        while lo < hi:
            best = max(best, (hi-lo)*min(heights[lo], heights[hi]))
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        return best

    #O(n), O(n)    