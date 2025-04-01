from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.quad = []

    def twoSum(self, nums, start, target):
        left, right = start, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                self.result.append(self.quad + [nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    def kSum(self, nums, k, start, target):
        if k == 2:
            self.twoSum(nums, start, target)
        else:
            for idx in range(start, len(nums) - k + 1):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                self.quad.append(nums[idx])
                self.kSum(nums, k - 1, idx + 1, target - nums[idx])
                self.quad.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.kSum(nums, 4, 0, target)
        return self.result


def main():
    target = Solution()

    nums = [-2, -1, -1, 1, 1, 2, 2]
    output = target.fourSum(nums, target=0)
    print(output)


if __name__ == "__main__":
    main()
