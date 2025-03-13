from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numMap = {}

        for idx, num in enumerate(nums):
            numMap[num] = idx

        for target_idx in range(len(nums) - 2):
            for num_idx in range(target_idx + 1, len(nums)):
                complement = -1 * (nums[target_idx] + nums[num_idx])
                if complement in numMap and numMap[complement] not in [target_idx, num_idx]:
                    triplet = sorted([nums[target_idx], complement, nums[num_idx]])
                    if triplet not in results:
                        results.append(triplet)
                numMap[nums[num_idx]] = num_idx
        return results


def main():
    target = Solution()
    result = target.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)


if __name__ == "__main__":
    main()
