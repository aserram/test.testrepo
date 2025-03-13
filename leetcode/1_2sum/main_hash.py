from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        numMap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], idx]
            numMap[num] = idx
        return []


def main():
    target = Solution()
    result = target.twoSum([2, 7, 11, 15], 18)
    print(result)


if __name__ == "__main__":
    main()
