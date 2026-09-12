from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in values:
                return [values[complement], i]
            values[num] = i

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))