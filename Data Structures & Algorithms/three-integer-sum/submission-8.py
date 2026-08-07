class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            lo, hi = i+1, len(nums) - 1
            while lo < hi:
                s = nums[lo] + nums[hi] + nums[i]
                if s<0:
                    lo += 1
                elif s>0:
                    hi -= 1
                else:
                    res.add((nums[i], nums[lo], nums[hi]))
                    lo+=1
                    hi-=1
        return [list(t) for t in res]

