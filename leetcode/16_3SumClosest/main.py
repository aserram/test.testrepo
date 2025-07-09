import json
from typing import List
import timeit


class jsonReader:
    def read(self, file: str) -> List[int]:
        with open(file) as numlist:
            jsonObject = json.load(numlist)
        return jsonObject["nums"]


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        if target < closest_sum:
            return closest_sum

        for third_idx, third_num in enumerate(nums):
            left, right = third_idx + 1, len(nums) - 1

            if third_num == nums[third_idx - 1] and third_idx > 0:
                continue

            while left < right:
                three_sum = third_num + nums[left] + nums[right]

                if three_sum == target:
                    return three_sum

                if abs(closest_sum - target) > abs(three_sum - target):
                    closest_sum = three_sum
                    pass

                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1

        return closest_sum


def main():
    reader = jsonReader()
    target = Solution()

    nums = reader.read("leetcode\\15_3sum\\nums.txt")
    # nums_edgecase = [-10, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
    nums_edgecase = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    result = target.threeSumClosest(nums_edgecase, 12)
    print(result)


if __name__ == "__main__":
    n = 1
    result = timeit.timeit(stmt="main()", globals=globals(), number=n)
    print(f"Execution time is {1000*(result/n)}ms")
