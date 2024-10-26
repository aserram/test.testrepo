from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        runningnums = []
        running = 0
        for num in nums:
            running += num
            runningnums.append(running)
        return runningnums

def main():
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    running = solution.running_sum(nums)
    print(running)

if __name__ == "__main__":
    main()
