class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums))!=len(nums)

print(Solution().containsDuplicate(nums=[1, 2, 3, 1]))