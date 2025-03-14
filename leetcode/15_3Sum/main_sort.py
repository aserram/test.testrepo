from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for target_idx, target in enumerate(nums):
            left, right = target_idx + 1, len(nums) - 1
            if target_idx > 0 and target == nums[target_idx - 1]:
                continue
            while left < right:
                three_sum = target + nums[right] + nums[left]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    results.append([target, nums[right], nums[left]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results


def main():
    target = Solution()
    result = target.threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10])
    print(result)


if __name__ == "__main__":
    main()
