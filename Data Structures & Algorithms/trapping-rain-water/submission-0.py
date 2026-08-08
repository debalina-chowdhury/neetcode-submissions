class Solution:
    def trap(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        lmax = rmax = water = 0
        while lo < hi:
            if height[lo] < height[hi]:
                lmax = max(lmax, height[lo])
                water += lmax - height[lo]
                lo += 1
            else:
                rmax = max(rmax, height[hi])
                water += rmax - height[hi]
                hi -= 1
        return water