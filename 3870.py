class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)


t = Solution()
print(t.countCommas(1000))