from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_vol = 0
        while left < right:
            container_height = min(height[left], height[right])
            current_vol = container_height * (right - left)
            max_vol = max(max_vol, current_vol)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_vol


def main():
    target = Solution()
    container = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_vol = target.maxArea(container)
    print(max_vol)


if __name__ == "__main__":
    main()
