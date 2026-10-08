class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        stop = len(nums) -1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else :
                stop = mid - 1
        return start

print(Solution().searchInsert([1, 3, 5, 7], target=5))