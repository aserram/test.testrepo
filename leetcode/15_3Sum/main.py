from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numMap = {}
        nums.sort()

        for idx, num in enumerate(nums):
            numMap[num] = idx

        for target_idx in range(len(nums) - 2):
            if target_idx > 0 and nums[target_idx] == nums[target_idx - 1]:
                continue
            for num_idx in range(target_idx + 1, len(nums)):
                complement = (-1 * nums[target_idx]) - nums[num_idx]
                if complement in numMap and numMap[complement] not in [target_idx, num_idx]:
                    triplet = [nums[target_idx], complement, nums[num_idx]]
                    if triplet not in results:
                        results.append(triplet)
                numMap[nums[num_idx]] = num_idx
        return results


def main():
    target = Solution()
    result = target.threeSum([0, 0, 0])
    print(result)


if __name__ == "__main__":
    main()
