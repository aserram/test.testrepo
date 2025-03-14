from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right, left = 0, len(numbers) - 1

        while right < left:
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [right + 1, left + 1]

            if sum > target:
                left -= 1
            else:
                right += 1
        return []


def main():
    target = Solution()
    # result = target.twoSum([2, 7, 11, 15], 9)
    # result = target.twoSum([2,3,4], 6)
    result = target.twoSum([-1, 0], -1)
    print(result)


if __name__ == "__main__":
    main()
