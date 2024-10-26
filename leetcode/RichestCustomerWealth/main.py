from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            wealth = 0
            for money in account:
                wealth += money
            richest = max(richest, wealth)

        return richest

def main():
    accounts = [[1,2,3],[3,2,1], [3,4,5]]
    solution = Solution()
    richest = solution.maximumWealth(accounts)
    print(richest)

if __name__ == "__main__":
    main()
