class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        result = 0

        while left <= right:
            middle = (left + right) // 2

            if middle <= x // middle:
                result = middle
                left = middle + 1
            else:
                right = middle - 1

        return result


s = Solution()
print(s.mySqrt(8))