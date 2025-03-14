from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []


def main():
    target = Solution()
    # result = target.twoSum([2, 7, 11, 15], 9)
    # result = target.twoSum([2,3,4], 6)
    result = target.twoSum([-1, 0], -1)
    print(result)


if __name__ == "__main__":
    main()
