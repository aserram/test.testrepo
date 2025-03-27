from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.quad = []

    def two_sum(self, nums, left, right, target):
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                self.results.append(self.quad + [nums[left], nums[right]])
                left += 1
                while nums[left - 1] == nums[left] and left < right:
                    left += 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

    def k_sum(self, k, nums, start, target):
        if k == 2:
            self.two_sum(nums, start, len(nums) - 1, target)
        else:
            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                self.quad.append(nums[idx])
                self.k_sum(k - 1, nums, idx + 1, target - nums[idx])
                self.quad.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.k_sum(4, nums, 0, target)

        return self.results


def main():
    target = Solution()
    # nums = [1, 0, -1, 0, -2, 2]
    # nums = [2, 2, 2, 2, 2]
    nums = [-2, -1, -1, 1, 1, 2, 2]
    output = target.fourSum(nums, target=0)
    print(output)


if __name__ == "__main__":
    main()
