import json
from typing import List
import timeit


class jsonReader:
    def read(self, file: str) -> List[int]:
        with open(file) as numlist:
            jsonObject = json.load(numlist)
        return jsonObject["nums"]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for target_idx, target in enumerate(nums):
            left, right = target_idx + 1, len(nums) - 1
            if target_idx > 0 and target == nums[target_idx - 1]:
                continue
            while left < right:
                three_sum = target + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    results.append([target, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results


def main():
    reader = jsonReader()
    target = Solution()

    nums = reader.read("leetcode\\15_3sum\\nums.txt")
    # nums_edgecase = [-10, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
    result = target.threeSum(nums)
    print(result)


if __name__ == "__main__":
    n = 1
    result = timeit.timeit(stmt="main()", globals=globals(), number=n)
    print(f"Execution time is {1000*(result/n)}ms")
