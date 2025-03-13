from typing import List
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        for first_idx in range(len(nums) - 1):
            for second_idx in range(first_idx + 1, len(nums)):
                if nums[first_idx] + nums[second_idx] == target:
                    return [first_idx, second_idx]
        return []


def main():
    target = Solution()
    result = target.twoSum([-1, 0, 1, 2, -1, -4], -5)
    print(result)


if __name__ == "__main__":
    main()
