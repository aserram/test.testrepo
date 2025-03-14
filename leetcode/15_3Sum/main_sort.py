from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for target_idx in range(len(nums) - 2):
            left, right = target_idx + 1, len(nums) - 1
            if target_idx > 0 and nums[target_idx] == nums[target_idx - 1]:
                continue
            while left < right:
                sum = nums[right] + nums[left]
                if nums[target_idx] + sum == 0:
                    triplet = [nums[target_idx], nums[left], nums[right]]
                    if triplet not in results:
                        results.append(triplet)
                    right -= 1
                    left += 1
                elif nums[target_idx] + sum > 0:
                    right -= 1
                else:
                    left += 1

        return results


def main():
    target = Solution()
    result = target.threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10])
    print(result)


if __name__ == "__main__":
    main()
