from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        maxHeight = max(height)
        while left < right:
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if maxArea >= maxHeight * (right - left):
                break

        return maxArea

    def maxAreaV2(self, height: List[int]) -> int:
        # 暴力枚举 超时
        maxArea = 0
        maxHeight = max(height)

        for i in range(len(height)):
            for j in range(len(height)):
                maxArea = max(maxArea, abs(j - i) * min(height[i], height[j]))
                if maxArea >= maxHeight * abs(j - i):
                    break

        return maxArea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxAreaV2(height))