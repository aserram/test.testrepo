from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        results = []

        for idx_four, num_four in enumerate(nums):
            if idx_four > 0 and nums[idx_four - 1] == num_four:
                continue

            for idx_three, num_three in enumerate(nums[idx_four + 1 : len(nums) - 1], start=idx_four + 1):
                if idx_three > 0 and nums[idx_three - 1] == num_three:
                    continue

                left, right = idx_three + 1, len(nums) - 1
                while left < right:
                    four_sum = num_four + num_three + nums[left] + nums[right]
                    if four_sum == target:
                        results.append([num_four, num_three, nums[left], nums[right]])
                        left += 1
                        while nums[left - 1] == nums[left] and left < right:
                            left += 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1


def main():
    target = Solution()
    output = target.fourSum([1, 0, -1, 0, -2, 2], target=0)
    print(output)


if __name__ == "__main__":
    main()
