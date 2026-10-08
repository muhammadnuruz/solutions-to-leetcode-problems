class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = dict()
        for i in range(len(nums)):
            c = target - nums[i]
            if c in nums:
                return [m[c], i]
            m[nums[i]] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))