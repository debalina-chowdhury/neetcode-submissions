class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(numbers):
            complement = target - value
            if complement in seen:
                return [seen[complement] + 1, index + 1]
            seen[value] = index
        return []

    #O(n), O(n)